"""
Numero de programa:04
Nombre:Diego Alonso Aragón Villarreal
Matricula:361349
Fecha ultima de modificación:27/02/2020
Razón de modificación:Creacion
"""
"""
Clases:
    Rangos
        sumatoria
        promedio
        archivoAArreglo
        arregloALn
        calcularVariante
        calcularDesviacionEstandar
        calcularResultadosLogaritmoNatural
        calcularResultados
        imprimir

"""
import sys
import math
class Rangos:
    setDeResultados=[]
    setDeDatos=[]
    setDeLn=[]

    def sumatoria(self,arr):
        """

        """
        return sum(arr)

    def promedio(self,arr):
        """

        """
        return(self.sumatoria(arr)/len(arr))

    def archivoAArreglo(self,archivo):
        """

        """
        pass

    def arregloALn(self,arr):
        """

        """
        self.setDeLn=[math.log(numero) for numero in self.setDeDatos]

    def calcularVariante(self):
        """

        """
        pass

    def calcularDesviacionEstandar(self):
        """

        """
        return math.sqrt(self.calcularVariante())

    def calcularResultadosLogaritmoNatural(self):
        """

        """
        arrDeResultados=[]
        desviacionEstandar=self.calcularDesviacionEstandar()
        promedio=self.promedio(self.setDeLn)
        arrDeResultados.append(promedio-(2*desviacionEstandar))
        arrDeResultados.append(promedio-desviacionEstandar)
        arrDeResultados.append(promedio)
        arrDeResultados.append(promedio+desviacionEstandar)
        arrDeResultados.append(promedio+(2*desviacionEstandar))
        self.setDeResultados=arrDeResultados

    def calcularResultados(self):
        """

        """
        self.setDeResultados=[math.exp(numero) for numero in self.setDeResultados]
    
    def imprimir(self):
        """

        """
        pass

    def __init__(self,archivo):
        """

        """
        pass

if __name__ == "__main__":
    archivo = str(sys.argv[1])