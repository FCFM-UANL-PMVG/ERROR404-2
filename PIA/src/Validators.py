import re

def es_año_valido(texto):
    patron = r"^\d{4}$" 
    return bool(re.match(patron, str(texto)))

def es_enlace_valido(url):
    patron = r"^https?://.+"
    return bool(re.match(patron, url)) 
