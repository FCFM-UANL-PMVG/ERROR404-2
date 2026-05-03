# ERROR404-2
### Equipo: 
- Berrones Avila Iñaqui Emiliano 2274523
- Morales Maldonado Isis Amithaba Madai, 2195272.

### Pregunta de investigación: 
¿En qué año se subieron más artículos a Google Scholar: 2001, 2008? 

### Justificación: 
Buscamos saber en qué año se hizo más investigación para relacionarlo con el avance del tiempo.

## DOCUMENTACIÓN: 
https://serpapi.com/google-scholar-organic-results
- API: SerpApi usando Google Scholar
- url: "https://serpapi.com/search.json"
- Endpoints: _scholar

### PARAMÉTROS DEL API:
- q: obligatorio, define lo que quieres buscar.
- cites: define un ID para un artículo para activar las búsquedas dentro de "Cited by"(Citado por). Al combinarlo con "q" activa la búsqueda dentro de los artículos que citan. 
- as_ylo: opcional, define un año para excluir los resultados anteriores al elegido.
- as_yhi: opcional, define un año para excluir los resultados posteriores al elegido.
- cluster: opcional, define un ID para un artículo buscado en All Versions (Todas las Versiones). No se puede mezclar con "q" ni "cites".
- hl: idioma, para el español es "es".

### PARAMÉTROS DE SERPAPI:
- engine: escoge el motor para usar el API de Google Scholar.
- clave_api: define la clave privada de SerpApi que se va a utilizar.
