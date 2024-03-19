
from loader import load_document
from splitter import split_document

class DocumentRepository:
    def __init__(self, search_model, rerank_model, util, top_k):
        self.documents = []
        self.search_model = search_model
        self.rerank_model = rerank_model
        self.util = util
        self.top_k = top_k

    def store(self, pdf_path):
        document = load_document(pdf_path)
        splitted_documents = split_document(document)
        document_embeddings = self.search_model.encode(splitted_documents, convert_to_tensor=True)
        for i in range(len(splitted_documents)):
            self.documents.append({
                "source" : pdf_path,
                "index" : i,
                "content" : splitted_documents[i],
                "embedding" : document_embeddings[i]
            })


    def query(self, query):
        document_embeddings = [document["embedding"] for document in self.documents]
      
        query_embeddings = self._create_query_embeddings(query)
    
        hits = self.util.semantic_search(query_embeddings, document_embeddings, top_k=self.top_k)
        hits = hits[0]  
        top_k_hits = hits[0:self.top_k]
        top_k_pairs = [[query, self.documents[hit["corpus_id"]]["content"]] for hit in top_k_hits]
        reranked_scores = self.rerank_model.predict(top_k_pairs)
        
        for idx in range(len(top_k_hits)):
            top_k_hits[idx]["score"] = reranked_scores[idx]

        reranked_hits = sorted(top_k_hits, key=lambda x: x["score"], reverse=True)

        result = []
        for reranked_hit in reranked_hits:
            document = self.documents[reranked_hit["corpus_id"]]
            result.append({
                "score" :  reranked_hit["score"],
                "document" : document
            })

        return result
       

      
    def _create_query_embeddings(self, query):
        return self.search_model.encode(query, convert_to_tensor=True)