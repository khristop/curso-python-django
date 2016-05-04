
#Encapsulacion --> se logra con los modificadores de acceso en java, c++

#No existe modificadores de acceso

class Ejemplo:
    #metodo publico
    def publico(self):
        print("publico")
    #Metodo privados se define con doble guion bajo
    def __privado(self):
        print("privado")
            
ej=Ejemplo()
ej.publico()

#NO EXISTEN MODIFICADORES DE ACCESO, ESTA TRAMPA ES POSIBLE QUITARLA
#MEDIANTE EL SIGUIENTE TRUCO
ej._Ejemplo__privado()

# dara error al ejecutar el metodo privado
print("la invocacion ej.__privado() Dara error, ya que es privado, revisa como se quita esta trampa")
print("en el codigo, que es un truco para descubrir que no hay modificadores de acceso")
ej.__privado()


            
