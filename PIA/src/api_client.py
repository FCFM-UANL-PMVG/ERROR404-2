import requests
import json

def get_data(url, etro):
    try:
        response = requests.get(url, params=etro)
        if response.status_code == 200:
            print("Conexión exitosa")
            data = response.json()
            crudo = data.get("organic_results", [])
            
            with open("entregable_01/raw/response.json", "a", encoding="utf-8") as f:
                json.dump(crudo, f, indent=4)
                f.write("\n")
                print(f"Json creado")
            return crudo, True
        else:
            return False, f"Error en la API: {response.status_code}"
    except Exception as fries:
        return False, f"Error de conexión: {fries}"
