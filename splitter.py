from langchain_text_splitters import RecursiveCharacterTextSplitter


def split_document(document):
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100,
        length_function=len,
        is_separator_regex=False,
    )
    texts = text_splitter.split_text(document)
    return texts

