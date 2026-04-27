import requests
import json

url = "https://serpapi.com/search.json"
api_key = " "

bus_params = {
    "engine": "google_scholar",
    "q": "2001",
    "api_key": api_key,
    "hl": "es"
}
