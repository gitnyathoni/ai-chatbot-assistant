from langchain.vectorstores import Chroma
from langchain.embeddings import OpenAIEmbeddings
class RAGPipeline:
    def __init__(self, docs):
        self.db = Chroma.from_documents(docs, OpenAIEmbeddings())
    def retrieve(self, query, k=5):
        return self.db.similarity_search(query, k=k)
