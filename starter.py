from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.llms.ollama import Ollama
from llama_index.vector_stores.chroma import ChromaVectorStore

from llama_index.core import (
    SimpleDirectoryReader, 
    VectorStoreIndex, 
    Settings, 
    StorageContext,
    load_index_from_storage,
)
import chromadb

PERSIST_DIR = "./chroma_db"
DATA_DIR = "./cd_data"
MODEL = "mistral"
COLLECTION = "doctorow"

ollama_embedding = OllamaEmbedding(
    model_name=MODEL,
    base_url="http://localhost:11434",
    # ollama_additional_kwargs={"mirostat": 0},
)
llm = Ollama(model=MODEL,
             request_timeout=300.0
)
Settings.llm = llm
Settings.embed_model = ollama_embedding

chroma_client = chromadb.PersistentClient(path=PERSIST_DIR)

try:
    chroma_collection = chroma_client.get_collection(COLLECTION)
    vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
    index = VectorStoreIndex.from_vector_store(vector_store, embed_model=ollama_embedding)
except:
    chroma_collection = chroma_client.get_or_create_collection(COLLECTION)
    documents = SimpleDirectoryReader(DATA_DIR).load_data()
    vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
    storage_context = StorageContext.from_defaults(vector_store=vector_store)
    index = VectorStoreIndex.from_documents(documents, storage_context=storage_context, embed_model=ollama_embedding)
    #index.storage_context.persist()

query_engine=index.as_query_engine()

while True:
    q = input("--> ")
    if q == '':
        break
    response = query_engine.query(q)
    print(response)
