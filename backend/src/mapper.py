"""
mapper.py
Plots events on a map and calculates commute distances.
"""

import folium
from geopy.geocoders import Nominatim

geolocator = Nominatim(user_agent="event-mapper")

def get_coordinates(address: str):
    """
    Convert address to (lat, lon).
    """
    loc = geolocator.geocode(address)
    if loc:
        return (loc.latitude, loc.longitude)
    return None

def create_map(events: list[dict], base_location: str = "San Francisco, CA"):
    """
    Create interactive map with event markers.
    """
    base_coords = get_coordinates(base_location) or (37.7749, -122.4194)
    m = folium.Map(location=base_coords, zoom_start=12)

    for e in events:
        coords = get_coordinates(e.get("location", base_location))
        if coords:
            folium.Marker(coords, popup=e["title"]).add_to(m)

    m.save("map.html")
    return "map.html"
