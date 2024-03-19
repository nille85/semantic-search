from document_repository import DocumentRepository
from sentence_transformers import SentenceTransformer, util

search_model = SentenceTransformer("all-MiniLM-L6-v2")
from sentence_transformers.cross_encoder import CrossEncoder
rerank_model = CrossEncoder("cross-encoder/stsb-roberta-base")
top_k = 15

if __name__ == "__main__":
    pdf_path = "input/report.pdf"
    repository = DocumentRepository(search_model, rerank_model, util, top_k)
    repository.store(pdf_path)

    query = "What is the proposed technology strategy?"
    documents = repository.query(query)
    for document in documents:
        doc = document["document"]
        print(f'Source: {doc["source"]},index: {doc["index"]}')
        print("Content:")
        print(f'{doc["content"]}')
        print("\r\n")
        print("----------------------------------")
        print("\r\n")
        
  

