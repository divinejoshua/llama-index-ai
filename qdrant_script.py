import logging
import sys
import os

import qdrant_client
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.core import StorageContext
from llama_index.vector_stores.qdrant import QdrantVectorStore
from llama_index.embeddings.fastembed import FastEmbedEmbedding
from llama_index.core import Settings

# Settings.embed_model = FastEmbedEmbedding(model_name="BAAI/bge-base-en-v1.5")

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")


client = qdrant_client.QdrantClient(
    # you can use :memory: mode for fast and light-weight experiments,
    # it does not require to have Qdrant deployed anywhere
    # but requires qdrant-client >= 1.1.1
    # location=":memory:"
    # otherwise set Qdrant instance address with:
    url=os.getenv("QDRANT_URL"),
    # otherwise set Qdrant instance with host and port:
    # host="localhost",
    # port=6333
    # set API KEY for Qdrant Cloud
    api_key=os.getenv("QDRANT_API_KEY"),
)



# load documents
documents = SimpleDirectoryReader("./paul_g").load_data()

vector_store = QdrantVectorStore(client=client, collection_name="paul_graham")
storage_context = StorageContext.from_defaults(vector_store=vector_store)
index = VectorStoreIndex.from_documents(
    documents,
    storage_context=storage_context,
)



# set Logging to DEBUG for more detailed outputs
query_engine = index.as_query_engine()
response = query_engine.query("What did the author do growing up?")

print(response)