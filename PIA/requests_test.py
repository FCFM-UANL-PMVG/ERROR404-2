import requests
import json
import os

url = "https://serpapi.com/search.json"
api_key = " "

bus_params = {
    "engine": "google_scholar",
    "q": "2001",
    "api_key": api_key,
}
#==================================================================
try:
  response = requests.get(url, params=bus_params)
  if response.status_code == 200:
    print("Conexión exitosa")
  else:
    print("Error en la API:", response.status_code)
except Exception as fries:
  print("Error de conexión:", fries)
  
#==============================================================
if not os.path.exists("data/raw"):
  os.makedirs("data/raw")
    
if response.status_code == 200:
  data = response.json()
    with open("data/raw/answer.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)
else:
    print("Error:", response.status_code)
