"""
api.py
Exposes FastAPI endpoints for querying events + maps.
"""

from fastapi import FastAPI
from src.scraper import fetch_eventbrite_events
from src.rag_filter import index_events, query_events
from src.mapper import create_map

app = FastAPI()

@app.get("/events")
def get_events(keyword: str = "AI", location: str = "online"):
    events = fetch_eventbrite_events(keyword, location)
    index_events([e["title"] for e in events])
    results = query_events(keyword)
    return {"query": keyword, "results": results}

@app.get("/map")
def get_map(keyword: str = "AI", location: str = "San Francisco, CA"):
    events = fetch_eventbrite_events(keyword, location)
    map_file = create_map(events, base_location=location)
    return {"map_file": map_file}
