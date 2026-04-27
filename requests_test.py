import requests
import json

url = "https://serpapi.com/search.json"
api_key = "82d2f92aa54bfc77bbf0fa2943ae653ad77a8dc78b638dd5a605a5b3af8c1c2b"

bus_params = {
    "engine": "google_scholar",
    "q": "2001",
    "api_key": api_key,
    "hl": "es"
}
