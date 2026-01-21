class QueueError (IndexError):

    # La clase QueueError es una subclase de IndexError

    pass



class Queue:

    def __init__(self):
        self.__cola = []

    def __str__(self):
        return " ".join(self.__cola)
        
    def put(self, elemento):
        # Agrega elementos al principio de la lista
        self.__cola.insert(0, elemento)


    def get(self):
        # Elimina los elementos del final de la lista
        if(self.__cola == []):
            raise QueueError("NO se puede operar en una lista vacia")
        else:
            self.__cola.pop()
        

class SuperQueue(Queue):

    def is_vacia(self):
        if self.__cola == []:
            return True
        else:
            return False


cola = Queue()

# Agrega y elimina elementos a la cola
# Recoge el tratamiento de posibles excepciones
# que se pueden generar si la cola está vacía

try:
    cola.put("pepito")
    cola.put("llamo")
    cola.put("me")
    cola.put("hola")
    cola.get()
    cola.put("hola")
    print(cola.is_vacia())
    cola.get()
    cola.get()
    cola.get()
    cola.get()
    cola.get()
    print(cola.is_vacia())
    print(cola)
except QueueError as e:
    print(f"Error: {e}")
