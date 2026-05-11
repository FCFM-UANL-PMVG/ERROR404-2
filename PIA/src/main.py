import json
import os
from Cleaner import limpiar_articulo
from Validators import es_enlace_valido
from api_client import get_data
from excel_utils import generar_excel_actividad 

URL = "https://serpapi.com/search.json"
API_KEY = "82d2f92aa54bfc77bbf0fa2943ae653ad77a8dc78b638dd5a605a5b3af8c1c2b"
JSON_TEMP = "data/clean/data_clean.json"
EXCEL_FINAL = "results/datos.xlsx" 

articulos = {
    "por_año": {},
    "total": {"autores": [], "tipos": []},
    "publicaciones_por_año": []
}

fechas = [2001, 2002, 2003, 2004, 2005, 2006, 2007, 2008]

os.makedirs("data/clean", exist_ok=True)

print("Iniciando extracción de datos...")

for año in fechas:
    if año not in articulos["por_año"]:
        articulos["por_año"][año] = {"autores": [], "tipos": []}
    
    registrado_total_año = False

    for pagina in range(0, 100, 10):
        params = {
            "engine": "google_scholar",
            "q": "salud",
            "as_ylo": año,
            "as_yhi": año,
            "start": pagina,
            "api_key": API_KEY,
        }

        if es_enlace_valido(URL):
            crudo, pub, exito = get_data(URL, params)
            if exito:
                if not registrado_total_año:
                    articulos["publicaciones_por_año"].append({"Año": año, "Cantidad": pub})
                    registrado_total_año = True
                
                for item in crudo:
                    limpio = limpiar_articulo(item)
                    t = limpio.get("tipo")
                    articulos["por_año"][año]["tipos"].append(t)
                    articulos["total"]["tipos"].append(t)
                    
                    for autor in limpio.get("autores", []):
                        if autor != "Desconocido":
                            articulos["por_año"][año]["autores"].append(str(autor))
                            articulos["total"]["autores"].append(str(autor))
            else:
                break
        else:
            break

with open(JSON_TEMP, "w", encoding="utf-8") as f:
    json.dump(articulos, f, indent=4, ensure_ascii=False)

generar_excel_actividad(JSON_TEMP, EXCEL_FINAL)

print("¡Proceso terminado!")
