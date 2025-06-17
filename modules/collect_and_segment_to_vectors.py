import chromadb
from .wikipedia_search import get_wikipedia_content
from .embedding import get_embedding

def collect_and_segment_to_vectors(topic):
    content = get_wikipedia_content(topic)
    (chroma_client, chroma_collection) = init_chroma()
    embedding_collection = get_embedding(content)
    chroma_collection.upsert(documents=content, ids=["test"], embeddings=[embedding_collection.embedding])
    return (chroma_client, chroma_collection)

def init_chroma():
    client = chromadb.PersistentClient(path="./vector-db")
    collection = client.get_or_create_collection("my_collection")
    return (client, collection)
        
