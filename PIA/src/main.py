import requests
import re
import json
import os
from Cleaner import limpiar_articulo
from Validators import es_enlace_valido
from api_client import get_data

url = "https://serpapi.com/search.json"
api_key = ""
articulos = {
    "tipo": [],
    "autores": [],
}

fechas_investigadas = [2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008]

if os.path.exists("data/raw") == False:
      os.makedirs("data/raw")
if os.path.exists("data/clean") == False:
      os.makedirs("data/clean")


for fecha in fechas_investigadas:
    for pagina in range(0, 100, 10):
        etro = {
            "engine": "google_scholar",
            "q": "salud",
            "as_ylo": fecha,
            "as_yhi": fecha,
            "start": pagina,
            "api_key": api_key,
        }
#=====================================================
        url_valido = es_enlace_valido(url)
        if url_valido == True:
            crudo, prueba = get_data(url, etro)
            if prueba == True:
                for i in crudo:
                    item_limpio = limpiar_articulo(i)
                    artículos["tipo"].append(item_limpio["tipo"])
                    for autor in item_limpio["autores"]:
                        if autor != "Desconocido":
                            articulos["autores"].append(autor)
            else:
                print(prueba)
                break
        else:
            print(prueba)
            break

with open("data/clean/data_clean.json", "w", encoding="utf-8") as f:
      json.dump(articulos, f, indent=4, ensure_ascii=False)

print(json.dumps(articulos, indent=4, ensure_ascii=False))
