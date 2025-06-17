import chromadb
from .wikipedia_search import get_wikipedia_content
from .chunking import get_chunks_of_text
from .embedding import get_embedding, get_embeddings

def collect_and_segment_to_vectors(topic):
    content = get_wikipedia_content(topic)
    (chroma_client, chroma_collection) = init_chroma()
    chunks = get_chunks_of_text(content)
    chunks_text = [chunk.page_content for chunk in chunks]
    embedding_collection = get_embeddings(chunks_text)
    for i in range(0, len(embedding_collection)):
        chroma_collection.upsert(documents=chunks_text[i],
                                 ids=[f"fact-{i+1}"],
                                 embeddings = [embedding_collection[i].embedding])
    return (chroma_client, chroma_collection)

def init_chroma():
    client = chromadb.PersistentClient(path="./vector-db")
    collection = client.get_or_create_collection("my_collection")
    return (client, collection)

def query(input:str, collection:chromadb.Collection):
    embedded_query = get_embedding(input)
    result = collection.query(query_embeddings=[embedded_query.embedding], n_results=2)
    print(result["documents"])
    print(result["distances"])
    return result
        
