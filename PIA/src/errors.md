##Manejo de errores
En api_client: 
• ConnectionError: error de conexión, error común en caso de no tener internet.
• RequestsException: se activa en caso de que el API no responda.
• Exception: cualquier otro y se menciona con un print para poder identificarlo y resolverlo.

En visualizations:
• FileNotFound: error común ql querer ejecutar sin que el Script1 haya recabado el diccionario que forma el json de donde obtiene la información 
