#Encapsulamiento

class Fecha():
    def __init__(self):
        self.__dia = 1
    def getDia(self):
        return self.__dia #revisa el ejemplo de encapsulamiento
    def setDia(self, dia):
        if dia > 0 and dia < 31:
            self.__dia = dia
            self.__printfecha()#Metodo estatico
        else:
            print("Error")
    def __printfecha(self):#metodo privado
        print("El dia del mes es:",self.__dia)

            
mi_fecha = Fecha()

mi_fecha.setDia(28)
