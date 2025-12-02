'''
===================================================================================================
= ------------------------------------ENCRIPTACIÓN DE CADENAS------------------------------------ =
===================================================================================================
'''


'''
------------------------------------SUSTITUCIONES------------------------------------
'''

def sustitucion1(msg, key):
    #suma el codigo de los caracteres de la clave
    #despues se lo suma a cada caracter de la cadena asegurando que esta en el rango 255
    suma = 0
    for i in key:
        suma += ord(i)
    msg = list(msg)
    msgcode = []
    for i in msg:
        i = chr((ord(i) + suma) % 255)
        msgcode.append(i)
    return "".join(msgcode)
def des_sustitucion1(msg, key):
    suma = 0
    for char in key:
        suma += ord(char)
    msg = list(msg)
    msgcode = []
    for i in msg:
        i = chr((ord(i) - suma) % 255)
        msgcode.append(i)
    return "".join(msgcode)


def sustitucion2(msg, key):
    #extrae el caracter con codigo más bajo de la clave y se lo resta a cada caracter de la cadena,
    #asegurando que esta en el rango 255
    n = ord(min(key))
    code = ''
    for i in msg:
        code += chr((ord(i) - n) % 255)
    return code
def des_sustitucion2(msg, key):
    n = ord(min(key))
    code = ''
    for i in msg:
        code += chr((ord(i) + n) % 255)
    return code


def sustitucion3(msg, key):
    #calcula la longitud de la clave y le suma 33
    #suma esa cifra a cada uno de los caracteres asegurando que este en el rango 255
    n = len(key) + 33
    code = ''
    for i in msg:
        code += chr((ord(i) + n) % 255)
    return code
def des_sustitucion3(msg, key):
    n = len(key) + 33
    code = ''
    for i in msg:
        code += chr((ord(i) - n) % 255)
    return code


def sustitucion4(msg, key):
    #extrae el codigo del primer caracter de la clave
    #suma esa cifra a cada uno de los caracteres del mensaje asegurando que este en el rango 255
    n = ord(key[0])
    code = ''
    for i in msg:
        code += chr((ord(i) + n) % 255)
    return code
def des_sustitucion4(msg, key):
    n = ord(key[0])
    code = ''
    for i in msg:
        code += chr((ord(i) - n) % 255)
    return code



'''
------------------------------------PERMUTACIONES------------------------------------
'''
def permutacion1(msg, key):
    #intercambia cada par de valores entre sí
    msg = list(msg)
    msgcode = ""
    for i in range(0, len(msg) - 1, 2):
        msg[i], msg[i+1] = msg[i+1], msg[i]
    return "".join(msg)
def des_permutacion1(msg, key):
    return permutacion1(msg, key)


def permutacion2(msg, key):
    #invierte el orden de la cadena por bloques definidos por la longitud de la clave
    n = len(key) // 3 #minimo5
    code = ""
    for i in range(0, len(msg), n):
        block = msg[i:i + n]
        code += block[::-1]
    return code
def des_permutacion2(msg, key):
    return permutacion2(msg, key)


def permutacion3(msg, key):
    #mueve el primer y el último caracter al final de la cadena
    if len(msg) < 2:
        return msg
    primer_char = msg[0]
    ultimo_char = msg[-1]
    #(cuerpo sin extremos) + (primer char) + (último char)
    return msg[1:-1] + primer_char + ultimo_char
def des_permutacion3(msg, key):
    if len(msg) < 2:
        return msg
    primer_char = msg[-2]
    ultimo_char = msg[-1]
    cuerpo = msg[:-2]
    return primer_char + cuerpo + ultimo_char


def permutacion4(msg, key):
    # invierte toda la cadena y luego la rota un número de posiciones basado en la clave
    n = (len(key) % 5) + 1 
    msg_invertida = msg[::-1]
    code = msg_invertida[-n:] + msg_invertida[:-n]
    return code

def des_permutacion4(msg, key):
    n = (len(key) % 5) + 1
    msg_desrotada = msg[n:] + msg[:n]
    descifrado = msg_desrotada[::-1]
    return descifrado

'''
------------------------------------ENCRIPTACIONES------------------------------------
'''
def validate(key):
    #La longitud de la clave no debe ser menor que 15 caracteres
    #y debe contener mayúsculas, minúsculas, dígitos y caracteres especiales.
    if (len(key) >= 15 and
        any(e.isupper() for e in key) and
        any(e.islower() for e in key) and
        any(e.isdigit() for e in key) and
        any(e in "!@#$%" for e in key)
    ):
        return True
    else:
        return False

def encryption(msg, key):
    # msg es el texto plano a encriptar
    # key es la clave a uƟlizar para encriptar
    # devuelve msg cifrado según key.
    if validate(key):
        msg = sustitucion1(msg, key)
        msg = sustitucion2(msg, key)
        msg = sustitucion3(msg, key)
        msg = sustitucion4(msg, key)
        msg = permutacion1(msg, key)
        msg = permutacion2(msg, key)
        msg = permutacion3(msg, key)
        msg = permutacion4(msg, key)
        return msg
    else:
        return "La clave no es correcta"

def decoded (msg, key):
    # msg es el texto cifrado a desencriptar
    # key es la clave a uƟlizar para desencriptar
    # devuelve msg decodificado según key.
    if validate(key):
        msg = des_permutacion4(msg, key)
        msg = des_permutacion3(msg, key)
        msg = des_permutacion2(msg, key)
        msg = des_permutacion1(msg, key)
        msg = des_sustitucion4(msg, key)
        msg = des_sustitucion3(msg, key)
        msg = des_sustitucion2(msg, key)
        msg = des_sustitucion1(msg, key)
        return msg
    else:
        return "La clave no es correcta"

'''
------------------------------------CASOS DE PRUEBA------------------------------------
'''

MENSAJES = [
    "Hola mundo! Estamos probando la criptografia.",
    "El cifrado es una herramienta esencial.",
    "Otro mensaje corto.",
    "Mensaje con acentos áéíóúÁÉÍÓÚñÑ" 
]

CLAVES_VALIDAS = [
    "Clave_1_MuySegura!@#$54321",
    "PruebaSegura123%abcdefghij"
]

CLAVE_INVALIDA = "clave_corta!1"

print("===================================================================\n")
print("========================INICIO DE LA PRUEBA========================\n")
print("===================================================================\n")
for i in range(len(MENSAJES)):
    for n in range(2):
        print(f"Mensaje a encriptar: {MENSAJES[i]}")
        print(f"Clave: {CLAVES_VALIDAS[n]}")
        encriptado = encryption(MENSAJES[i], CLAVES_VALIDAS[n])
        print(f"Mensaje encriptado: {encriptado}")
        print(f"Mensaje desencriptado: {decoded(encriptado, CLAVES_VALIDAS[n])}")
        print("===================================================================\n")

print("PRUEBA CLAVE INVALIDA")
print(f"Mensaje a encriptar: {MENSAJES[0]}")
print(f"Clave: {CLAVE_INVALIDA}")
encriptado = encryption(MENSAJES[i], CLAVE_INVALIDA)
print(f"Mensaje de ERROR del metodo encriptado: {encriptado}")
print(f"Mensaje de ERROR del metodo desencriptado: {decoded(encriptado, CLAVE_INVALIDA)}")
