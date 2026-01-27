class Empleado:
    def obtener_informacion():
        pass
    def calcular_sueldo():
        pass

class EmpleadoContratado(Empleado):
    def __init__(self,nombre, puesto, salario_base):
        self.__nombre = nombre
        self.__puesto = puesto
        self.__salario_base = salario_base

    def obtener_informacion(self):
        return f"Nombre: {self.__nombre} \n \
                 Puesto: {self.__puesto} \n \
                 Salario Base: {self.__salario_base}"        
    def calcular_sueldo(self):
        return self.__salario_base * 1.1

class EmpleadoExterno(Empleado):
    def __init__(self, nombre, puesto, horas, salario_por_hora):
        self.__nombre = nombre
        self.__puesto = puesto
        self.__horas = horas
        self.__salario_por_hora = salario_por_hora

    def obtener_informacion(self):
        return f"Nombre: {self.__nombre} \n \
                 Puesto: {self.__puesto} \n \
                 Horas Trabajadas: {self.__horas}\n \
                 Salario Por Hora: {self.__salario_por_hora}"
    def calcular_sueldo(self):
        return self.__horas * self.__salario_por_hora
    
e1 = EmpleadoExterno("Carmen", "Contable", 40, 10)
print(e1.calcular_sueldo())
print(e1.obtener_informacion())