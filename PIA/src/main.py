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
        
        if not os.path.exists("PIA/src"):
        os.makedirs("PIA/src")
        
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
        else:
       print(prueba)

print(json.dumps(articulos, indent=2, ensure_ascii=False))
