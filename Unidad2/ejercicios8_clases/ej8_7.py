class Stack:
    # Código del ejercicio 3 de la clase Queque.
    def __init__(self):
        self.__cola = []

    def __str__(self):
        return " ".join(self.__cola)
        
    def push(self, elemento):
        # Agrega elementos al principio de la lista
        self.__cola.insert(0, elemento)


    def pop(self):
        if not self._cola:
            raise Exception("No se puede operar en una lista vacía")
        return self._cola.pop()


class AddStack(Stack):
    def __init__(self):
        super().__init__()
        self.__contador = 0

    def getSum(self):
         return self.__contador

    def push(self, elemento):
        super().push(elemento) #llama al push() de queque
        self.__contador += 1

    def pop(self):
        valor = super().pop()   # <--- AQUÍ: Ejecuta el pop original (incluyendo el error)
        self.__contador -= 1    # Añade la línea extra
        return valor            # Devuelve el valor que sacó el padre



pila = AddStack()
pila.push("hola")
pila.push("adios")
pila.push("chao")
print(pila.getSum())
print(pila)
