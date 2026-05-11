import requests
import json
import os


def get_data(url, etro, fecha, pagina):
    try:
        response = requests.get(url, params=etro)

        if response.status_code == 200:
            print("Conexión exitosa")
            data = response.json()
            crudo = data.get("organic_results", [])
            publicaciones = data.get("search_information") or {}
            pub = publicaciones.get("data_results")

            ruta = "data/raw/response.json"
            os.makedirs(os.path.dirname(ruta), exist_ok=True)
            with open(ruta, "a", encoding="utf-8") as f:
                json.dump(crudo, f, indent=4)
                f.write("\n")
                print(f"Página guardada, artículos: {pagina}, año: {fecha}")

            return crudo, pub, True

        # Importante: devolver siempre booleano en el 3er valor
        return [], 0, False

    except requests.exceptions.ConnectionError as e:
        print(f"Error de conexión (ConnectionError): {e}")
        return [], 0, False
    except requests.exceptions.RequestException as e:
        print(f"Error de conexión (RequestException): {e}")
        return [], 0, False
    except Exception as e:
        print(f"Error inesperado: {e}")
        return [], 0, False

