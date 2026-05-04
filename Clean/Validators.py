import re #[cite: 154]

def es_año_valido(texto):
    patron = r"^\d{4}$" 
    return bool(re.match(patron, str(texto))) #[cite: 88, 161]

def es_enlace_valido(url):
    patron = r"^https?://.+"
    return bool(re.match(patron, url)) #[cite: 50, 178]


