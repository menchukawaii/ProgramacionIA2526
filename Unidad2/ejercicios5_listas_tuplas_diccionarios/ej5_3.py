'''
==============================EXPEDIENTE ALUMNO==============================

Tu tarea es escribir un pequeño traductor español-inglés. Debe leer una frase introducida
por el usuario y traducirla palabra por palabra. Si una palabra no está incluída en el
diccionario se mostrará sin traducir.

El diccionario con el vocabulario está implementado en el código.

Puede facilitarte el trabajo el empleo del método Split => Si frase es una cadena de caracteres,
el método frase.split() devuelve una lista de elementos, separando por defecto la
frase por espacios en blanco.
'''

diccionario_espanol_ingles = {
    "casa": "house",
    "perro": "dog",
    "gato": "cat",
    "sol": "sun",
    "luna": "moon",
    "agua": "water",
    "comida": "food",
    "libro": "book",
    "mesa": "table",
    "silla": "chair",
    "computadora": "computer",
    "telefono": "phone",
    "coche": "car",
    "calle": "street",
    "ciudad": "city",
    "país": "country",
    "gente": "people",
    "amigo": "friend",
    "familia": "family",
    "trabajo": "work",
    "escuela": "school",
    "universidad": "university",
    "mañana": "morning",
    "tarde": "afternoon",
    "noche": "night",
    "siempre": "always",
    "nunca": "never",
    "a veces": "sometimes",
    "rápido": "fast",
    "lento": "slow",
    "grande": "big",
    "pequeño": "small",
    "feliz": "happy",
    "triste": "sad",
    "caliente": "hot",
    "frío": "cold",
    "rojo": "red",
    "azul": "blue",
    "verde": "green",
    "amarillo": "yellow",
    "blanco": "white",
    "negro": "black",
    "cinco": "five",
    "diez": "ten",
    "cien": "hundred",
    "uno": "one",
    "dos": "two",
    "tres": "three",
    "cuatro": "four",
    "seis": "six",
    "siete": "seven",
    "ocho": "eight",
    "nueve": "nine",
    "comer": "to eat",
    "beber": "to drink",
    "dormir": "to sleep",
    "correr": "to run",
    "caminar": "to walk",
    "hablar": "to talk",
    "escribir": "to write",
    "leer": "to read",
    "ver": "to see",
    "escuchar": "to listen",
    "abrir": "to open",
    "cerrar": "to close",
    "empezar": "to start",
    "terminar": "to finish",
    "ayudar": "to help",
    "buscar": "to look for",
    "encontrar": "to find",
    "dar": "to give",
    "tomar": "to take",
    "venir": "to come",
    "ir": "to go",
    "hoy": "today",
    "ayer": "yesterday",
    "mañana (día)": "tomorrow",
    "problema": "problem",
    "solución": "solution",
    "historia": "history",
    "arte": "art",
    "ciencia": "science",
    "música": "music",
    "película": "movie",
    "juego": "game",
    "dinero": "money",
    "tiempo": "time",
    "mundo": "world",
    "vida": "life",
    "muerte": "death",
    "esperanza": "hope",
    "sueño": "dream",
    "verdad": "truth",
    "mentira": "lie",
    "fácil": "easy",
    "difícil": "difficult",
    "fuerte": "strong",
    "débil": "weak",
    "viaje": "trip",
    "puerta": "door",
    "ventana": "window","perro": "dog",
    "gato": "cat",
    "casa": "house",
    "pequeña": "small",
    "pequeño": "small",
    "comer": "to eat",
    "comida": "food",
    "caliente": "hot",
    "beber": "to drink",
    "agua": "water",
    "coche": "car",
    "rojo": "red",
    "grande": "big",
    "azul": "blue",
    "libro": "book",
    "ciencia": "science",
    "tarde": "afternoon",
    "tres": "three",
    "cinco": "five",
    "ocho": "eight",
    "solución": "solution",
    "fácil": "easy",
    
    
    # Palabras funcionales (la corrección)
    "el": "the",
    "la": "the",
    "un": "a",
    "una": "a",
    "y": "and",
    "en": "in",
    "pero": "but",
    "yo": "I",
    "ella": "she",
    "quiero": "want",
    "duermen": "sleep", # Verbo conjugado
    "es": "is",         # Verbo 'ser'
    "son": "are",       # Verbo 'ser'
    "empieza": "starts", # Verbo 'empezar'
    "a": "to",          # Preposición/Infinitivo
    "leer": "read",
    "sobre": "about",
    "busco": "look for", # Verbo 'buscar'
    "ocho": "eight"
}

FRASES_TRADUCCION_EXITOSA = [
    "El perro y el gato duermen en la casa pequeña",
    "Yo quiero comer comida caliente y beber agua",
    "El coche rojo es grande pero el coche azul es pequeño",
    "Ella empieza a leer un libro sobre ciencia en la tarde",
    "Tres y cinco son ocho . Busco una solución fácil"
]

FRASES_PALABRAS_FALTANTES = [
    "El astronauta vio la luna desde la nave espacial y sintió nostalgia",
    "Mi vecino está cocinando una cena deliciosa en la cocina",
    "La lluvia de primavera hizo crecer las flores moradas del jardín"
]


def traducir(frase, diccionario):
    frase_traducida = ""
    array_palabras = frase.split()
    for palabra in array_palabras:
        palabra = palabra.lower()
        if palabra in diccionario:
            frase_traducida += f"{diccionario[palabra]} "
        else:
            frase_traducida += f"''{palabra}'' "
    return frase_traducida


print("====================FRASES COMPLETAS====================")
for frase in FRASES_TRADUCCION_EXITOSA:
    print(f"Frase a traducir: {frase}")
    print(f"Frase traducida: {traducir(frase, diccionario_espanol_ingles)}\n")


print("====================FRASES CON PALABRAS FALTANTES====================")
for frase in FRASES_PALABRAS_FALTANTES: 
    print(f"Frase a traducir: {frase}")
    print(f"Frase traducida: {traducir(frase, diccionario_espanol_ingles)}\n")





