def limpiar_articulo(articulo):
    minaeli = ["position", "title", "result_id", "link", "snippet", "resources"]
    for campo in minaeli:
        if campo in articulo:
            del articulo[campo]
    autores_limpios = []
    if "publication_info" in articulo:
        autores = articulo["publication_info"].get("authors", [])
        for k in autores:
            nombre = k.get("name", "").strip().capitalize()
            if nombre:
                 autores_limpios.append(nombre)
    else:
        autores_limpios = ["Desconocido"]

    limpio = {
        "tipo": articulo.get("type"),
        "autores": autores_limpios
        }
    return limpio
