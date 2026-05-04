#=============================================================
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
#=============================================================

try:
  answer = requests.get(url, params=bus_params)
  if answer.status_code == 200:
    print("Conexión exitosa")
  else:
    print("Error en la API:", answer.status_code)
except Exception as fries:
  print("Error de conexión:", fries)
  
#==============================================================
if answer.status_code == 200:
    data = answer.json()

    with open("answer.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
else:
    print("Error:", answer.status_code)
