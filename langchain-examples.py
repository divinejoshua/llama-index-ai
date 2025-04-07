from langchain_community.document_loaders import UnstructuredPowerPointLoader
from langchain_community.document_loaders import DirectoryLoader
import time

# import nltk
# nltk.download('punkt')
# nltk.download('wordnet')
# nltk.download('omw-1.4')


start_time = time.time()

loader = DirectoryLoader("./data")
docs = loader.load()
print(f"Number of documents loaded: {len(docs)}")
print(docs)

end_time = time.time()
print(f"Time taken: {end_time - start_time} seconds")


# Powerpoint
# loader = UnstructuredPowerPointLoader("./data/presentation.pptx", mode='elements')

# data = loader.load()

# print(data)


# Word Document
# from langchain_community.document_loaders import UnstructuredWordDocumentLoader

# loader = UnstructuredWordDocumentLoader("data/word.docx")

# data = loader.load()

# print(data)


