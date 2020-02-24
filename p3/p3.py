"""
Numero de programa:03
Nombre:Diego Alonso Aragón Villarreal
Matricula:361349
Fecha ultima de modificación:24/02/2020
Razón de modificación:Creacion
"""
"""
Clases:
    Estimador(set1,set2):
        archivoAArreglo
        sumatoria
        promedio
        calculaB1
        calculaB0
        calculaR
        calculaRCuadrada
        calcularYResultante
        imprimir
        setXs
        setYs
        setXK
"""
import sys
import math

class Estimador:
    xK=0
    xs=[]
    ys=[]
    b0=0
    b1=0
    r=0
    yResultante=0
    def archivoAArreglo(self,nombreDeArchivo):
        """
            Esta funcion resive un path de un archivo
            regresa un arreglo con los numeros del archivo
        """
        return arreglo

    def sumatoria(self,arreglo):
        """
            Esta funcion resive un arreglo de numeros y regesa su sumatoria
        """
        return sum(arreglo)

    def promedio(self,arreglo):
        """
            Esta funcion resive un arreglo de numeros y regresa su promedio
        """
        return self.sumatoria(arreglo)/len(arreglo)

    def calculaB1(self):
        """
            Esta funcion calcula la b1 de dos sets de numeros
            al terminar guarda el resultado en la variable global b1
        """
        pass

    def calculaB0(self):
        """
            Esta funcion calcula la b0 de dos sets de numeros
            al terminar guarda el resultado en la variable global b0
        """
        pass

    def calculaR(self):
        """
            Esta funcion calcula la r de dos sets de numeros
            al terminar guarda el resultado en la variable global r
        """
        pass

    def calculaRCuadrada(self):
        """
            Esta funcion calcula la r**2 y la regresa
        """
        return self.r**2

    def calcularYResultante(self):
        """
            Esta funcion calcula la Y resultante y la guarda en la variable 
            global yResultante
        """
        self.calculaB1()
        self.calculaB0()
        self.yResultante = self.b0 + self.b1*self.xK

    def imprimir(self):
        """
            Esta funcion imprime toda la informacion de la clase
        """
        pass

    def setXs(self,arreglo):
        """
            Esta funcion resive un arreglo y lo guarda en la variable global
            xs
        """
        pass

    def setYs(self,arreglo):
        """
            Esta funcion resive un arreglo y lo guarda en la variable global
            ys
        """
        pass

    def setXK(self,xK):
        """
            Esta funcion resive un numero entero y lo guarda en la variable global
            xK
        """
        pass

    def __init__(self,archivoX,archivoY,xK=386):
        """
            Esta funcion es el constructor de la clase
        """
        self.setXs(self.archivoAArreglo(archivoX))
        self.setYs(self.archivoAArreglo(archivoY))
        self.setXK(xK)
        self.calcularYResultante()


if __name__ == "__main__":
    estimados=[]
    contador=0
    if(len(sys.argv)==4):
        archivo1 = str(sys.argv[1])
        archivo2 = str(sys.argv[2])
        xK=int(sys.argv[3])
        estimados.append(Estimador(archivo1,archivo2,xK))
    else:
        archivo1 = str(sys.argv[1])
        archivo2 = str(sys.argv[2])
        archivo3 = str(sys.argv[3])
        archivo4 = str(sys.argv[4])
        xK=int(sys.argv[5])
        estimados.append(Estimador(archivo1,archivo3,xK))
        estimados.append(Estimador(archivo1,archivo4,xK))
        estimados.append(Estimador(archivo2,archivo3,xK))
        estimados.append(Estimador(archivo2,archivo4,xK))

    for estimado in estimados:
        contador+=1
        print("estimado #"+contador)
        estimado.imprimir()
    