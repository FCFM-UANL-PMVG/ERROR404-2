import requests
import re
import json
import os
from Cleaner import limpiar_articulo
from validators import es_año_valido

url = "https://serpapi.com/search.json"
api_key = ""
articulos = []

for pagina in range(0, 100, 10):
    etro = {
        "engine": "google_scholar",
        "q": "salud",
        "as_ylo": 2001,
        "as_yhi": 2001,
        "start": pagina,
        "api_key": api_key, 
    }
    if not os.path.exists("PIA/src"):
        os.makedirs("PIA/src")
#=====================================================
    try:
        dosmiluno = requests.get(url, params=etro)
        if answer.status_code == 200:
            print("Conexión exitosa")
            data = dosmiluno.json()
            crudo = data.get("organic results", [])
            
            with open("PIA/src/dosmiluno.json", "a", encoding="utf-8") as f:
                json.dump(crudo, f, indent=4)
                f.write("\n")
                print("Json creado")
            for i in crudo:
                item_limpio = limpiar_articulo(i)
                articulos.append(item_limpio)
            print("Artículo limpios")
            print(json.dumps(articulos, indent=2, ensure_ascii=False))
    else:
    print("Error en la API:", answer.status_code)
except Exception as fries:
  print("Error de conexión:", fries)
  
