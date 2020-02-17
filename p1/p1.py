"""
Numero de programa:02
Nombre:Diego Alonso Aragón Villarreal
Matricula:361349
Fecha ultima de modificación:17/02/2020
Razón de modificación:estandar de codificacion
"""
"""
Clases:
    Lista():
        agregar
        sumatoria   
        calMedia
        sumatoriaMedia
        calDs
"""
import math

class Lista:
    numero=0
    lista=[]

    def agregar(self,numero):
        """
            Esta funcion resive un numero que se agregará a la lista dinamica
            no regresa nada
        """
        self.lista.append(numero)
        self.numero+=1

    def sumatoria(self):
        """
            Esta funcion hace una sumatoria de todos los elementos de la lista
            regresa el resultado de la sumatroia
        """
        total=0
        for i in self.lista:
            total+=i
        return total

    def calMedia(self):
        """
            Esta funcion calcula la media de la sumatoria
            regresa la media
        """
        return (self.sumatoria()/self.numero)

    def sumatoriaMedia(self):
        """
            Esta funcion calcula la sumatoria de cada elemento con respecto a la meida
            regresa la sumatoria
        """
        total=0
        avg=self.calMedia()
        for i in self.lista:
            total+=(i-avg)**2
        return total

    def calDesviacionEstandar(self):
        """
            Esta funcion calcula la Desviacion estandar de una sumatoria
            regresa el calculo
        """
        return math.sqrt(self.sumatoriaMedia()/(self.numero-1))

"""
Programa
"""
if __name__ == "__main__":
    l1=Lista()
    with open("test2.txt",'r') as fp:
        num = fp.readlines()
    for i in num:
            l1.agregar(float(i))

    print("Media:"+str(round(l1.calMedia(),2)))
    print("des. Estandar:"+str(round(l1.calDesviacionEstandar(),2)))