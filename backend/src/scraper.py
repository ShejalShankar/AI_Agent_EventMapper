"""
scraper.py
Handles fetching and parsing events from Meetup / Eventbrite
"""

import requests
from bs4 import BeautifulSoup

def fetch_eventbrite_events(keyword: str, location: str = "online") -> list[dict]:
    """
    Fetch events from Eventbrite search results.
    Args:
        keyword: Search term (e.g., "AI", "Machine Learning").
        location: City or 'online'.
    Returns:
        List of dicts with event details.
    """
    url = f"https://www.eventbrite.com/d/{location}/{keyword.replace(' ', '-')}/"
    resp = requests.get(url)
    soup = BeautifulSoup(resp.text, "html.parser")

    events = []
    for e in soup.select("div.eds-event-card-content__primary-content"):
        events.append({
            "title": e.get_text(" ", strip=True),
            # TODO: parse date, location, link
        })
    return events


if __name__ == "__main__":
    sample = fetch_eventbrite_events("AI")
    print(sample[:5])
