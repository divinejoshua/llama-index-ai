import os
import openai
from llama_index.vector_stores.neo4jvector import Neo4jVectorStore
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader

openai.api_key = os.getenv("OPENAI_API_KEY")
username = os.getenv("USERNAME")
password = os.getenv("PASSWORD")
url = os.getenv("NEO4J_URL")

embed_dim = 1536

neo4j_vector = Neo4jVectorStore(username, password, url, embed_dim)
# load documents
documents = SimpleDirectoryReader("./data").load_data()
from llama_index.core import StorageContext

storage_context = StorageContext.from_defaults(vector_store=neo4j_vector)
index = VectorStoreIndex.from_documents(
    documents, storage_context=storage_context
)

query_engine = index.as_query_engine()
response = query_engine.query("What happened at interleaf?")

print(response)