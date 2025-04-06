from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
# from IPython.display import Markdown, display
from llama_index.vector_stores.pinecone import PineconeVectorStore
from pinecone import Pinecone, ServerlessSpec
import os

os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# initialize without metadata filter
from llama_index.core import StorageContext

pc = Pinecone(api_key=os.getenv("PINECONE_API_KEY"))


index_id = "quickstart2"

# load documents
documents = SimpleDirectoryReader("./data").load_data()
print("Loaded documents: ", len(documents))

print("Creating index ")
# create index
pc.create_index(
    name=index_id,
    dimension=1536,
    spec=ServerlessSpec(cloud="aws", region="us-east-1"),
)

# print("Retrieving index ")
# initialize index
pinecone_index = pc.Index(index_id)


vector_store = PineconeVectorStore(pinecone_index=pinecone_index)
storage_context = StorageContext.from_defaults(vector_store=vector_store)

# index = VectorStoreIndex.from_documents(
#     documents, storage_context=storage_context
# )

# # Instantiate VectorStoreIndex object from your vector_store object
index = VectorStoreIndex.from_vector_store(vector_store=vector_store)




# set Logging to DEBUG for more detailed outputs
query_engine = index.as_query_engine()
response = query_engine.query("What was the adspend in q4 2024")

print(response)
