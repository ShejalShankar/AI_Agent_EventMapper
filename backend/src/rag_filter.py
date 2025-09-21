"""
rag_filter.py
Uses embeddings + vector search to filter relevant events.
"""

from sentence_transformers import SentenceTransformer
import chromadb

model = SentenceTransformer("all-MiniLM-L6-v2")
db = chromadb.Client()

def index_events(events: list[str]):
    """
    Add events to vector DB.
    """
    collection = db.get_or_create_collection("events")
    for event in events:
        emb = model.encode(event).tolist()
        collection.add(documents=[event], embeddings=[emb])

def query_events(query: str, n: int = 5):
    """
    Retrieve most relevant events for a query.
    """
    collection = db.get_or_create_collection("events")
    q_emb = model.encode(query).tolist()
    results = collection.query(query_embeddings=[q_emb], n_results=n)
    return results
