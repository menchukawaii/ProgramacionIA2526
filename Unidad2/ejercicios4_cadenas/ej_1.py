'''
Si las claves uƟlizadas para encriptar y desencriptar son diferentes se habla de criptograİa asimétrica. En 
caso contrario decimos que la criptograİa es simétrica.

Pide al usuario que ingrese la clave a utlizar. 

El resultado 
obtenido debe ser diferente si la clave es diferente. 

'''

#suma los el codigo de los caracteres de la clave
#despues se lo suma a cada caracter de la cadena  y lo divide entre 128    
def perm1(msg, key):
    suma = 0
    for char in key: #calcular el numero a sumar a partir de la clave
        suma += ord(char)
    msg = list(msg)
    msgcode = []
    for i in msg: #modificar el mensaje
        i = chr( (ord(i) + suma) % 128 )
        msgcode.append(i)
    return "".join(msgcode)

#suma los el codigo de los caracteres de la clave
#despues se lo resta a cada caracter de la cadena y lo divide entre 128    
def desperm1(msg, key):
    suma = 0
    for char in key: #calcular el numero a sumar a partir de la clave
        suma += ord(char)
    
    msg = list(msg)
    msgcode = []
    for i in msg: #modificar el mensaje
        i = chr( (ord(i) - suma) % 128 )
        msgcode.append(i)
    return "".join(msgcode)

def perm2(msg, key):
    msg = list(msg)
    msgcode = ""
    for i in range(0, len(msg), 2):
        msg[i], msg[i+1] = msg[i+1], msg[i]
    return "".join(msg)

def desperm2(msg, key):
    msg = list(msg)
    msgcode = ""
    for i in range(0, len(msg), 2):
        msg[i], msg[i+1] = msg[i+1], msg[i]
    return "".join(msg)




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


def encryption( msg, key ): 
    # msg es el texto plano a encriptar 
    # key es la clave a uƟlizar para encriptar
    # devuelve msg cifrado según key. 
    if validate(key):
        msg = perm1(msg, key)
        msg = perm2(msg, key)
        #msg = perm3(msg, key)
        #msg = perm4(msg, key)
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
        #msg = desperm3(msg, key)
        #msg = desperm4(msg, key)
        return msg
    else:
        return "La clave no es correcta"

mensaje = "quiero mucho al ronnie"
key = "Carmen123456789!"
 
print(encryption(mensaje, key))
code = encryption(mensaje, key)
print(decoded(code, key))

