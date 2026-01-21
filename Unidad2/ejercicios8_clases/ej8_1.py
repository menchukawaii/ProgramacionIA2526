class Timer:
    def __init__(self, horas, minutos, segundos):
        self.__horas = horas
        self.__minutos = minutos
        self.__segundos = segundos


    def __str__(self):
        # Para obtener hh:mm:ss
        horas = f"0{self.__horas}" if self.__horas < 10 else str(self.__horas)
        minutos = f"0{self.__minutos}" if self.__minutos < 10 else str(self.__minutos)
        segundos = f"0{self.__segundos}" if self.__segundos < 10 else str(self.__segundos)
        return f"{horas}:{minutos}:{segundos}"


    def next_second(self):
        self.__segundos += 1
        if self.__segundos > 59:
            self.__segundos = 0
            self.__minutos += 1
            if self.__minutos > 59:
                self.__minutos = 00
                self.__horas += 1
                if self.__horas > 23:
                    self.__horas = 0

    def prev_second(self):
        self.__segundos -= 1
        if self.__segundos < 0:
            self.__segundos = 59
            self.__minutos -= 1
            if self.__minutos < 0:
                self.__minutos = 59
                self.__horas -= 1
                if self.__horas < 0:
                    self.__horas = 23


timer = Timer(23, 59, 59)
print(timer)
timer.next_second()
print(timer)
timer.prev_second()
print(timer)

