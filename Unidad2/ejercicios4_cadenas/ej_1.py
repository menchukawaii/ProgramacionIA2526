'''
Si las claves uƟlizadas para encriptar y desencriptar son diferentes se habla de criptograİa asimétrica. En 
caso contrario decimos que la criptograİa es simétrica.

Pide al usuario que ingrese la clave a utlizar. 

El resultado 
obtenido debe ser diferente si la clave es diferente. 
'''

def validate(key):
    #La longitud de la clave no debe ser menor que 15 caracteres 
    #y debe contener mayúsculas, minúsculas, dígitos y caracteres especiales.
    if (len(key) >= 15 and
        any(e.isupper() for e in key) and #Verifica si CUALQUIER carácter en la cadena es mayúscula
        any(e.islower() for e in key) and #Verifica si CUALQUIER carácter en la cadena es minúscula
        any(e.isdigit() for e in key) and #Verifica si CUALQUIER carácter en la cadena es un numero
        any(e in "!@#$%" for e in key) #Verificar si CUALQUIER carácter en la cadena es un caracter especial    
    ):
        return True
    else:
        return False

def process_key(key):
    return processed

def perm1(msg, key):
    for i in msg:
        
    return 

def encryption( msg, key ): 
    # msg es el texto plano a encriptar 
    # key es la clave a uƟlizar para encriptar
    # devuelve msg cifrado según key. 
    if validate(key):
        msg = perm1(msg, key)
        msg = perm2(msg, key)
        msg = perm3(msg, key)
        msg = perm4(msg, key)
        return msg
    else:
        return "La clave no es correcta"

def decoded (msg, key):
    # msg es el texto cifrado a desencriptar 
    # key es la clave a uƟlizar para desencriptar 
    # devuelve msg decodificado según key.
    if validate(key):
        msg = desperm1(msg, key)
        msg = desperm2(msg, key)
        msg = desperm3(msg, key)
        msg = desperm4(msg, key)
        return msg
    else:
        return "La clave no es correcta"
    
    
print(validate("hola"))
print(validate("Hola"))
print(validate("hHola1234"))
print(validate("Hoooooooooola1234#"))
 
