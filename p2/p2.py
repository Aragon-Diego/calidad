"""
Numero de programa:02
Nombre:Diego Alonso Aragón Villarreal
Matricula:361349
Fecha ultima de modificación:17/02/2020
Razón de modificación:Creación
"""
"""
Clases:
    Programa(path):
        setPath
        programaALineas
        conteoModificadas
        conteoBase
        limpiarLineas
        conteoTotal
        conteoAgregado
        filtradoAClases

    Clase(arr):
        setArrLineasDelArchivo
        regresarCantidadDeFunciones
        regresarCantidadDeLineas
        conteoDeLineas
        conteoDeFunciones
"""
import sys

class Programa:
    clases=[]
    total=0
    agregadas=0
    modificadas=0
    base=0
    path=""
    arrLineasDelArchivo=[]
    arrDeLineasPorClase=[]

    def __init__(self,path):
        """
            esta funcion es el constructor de la clase.
        """
        setPath(path)

    def setPath(self,path):
        """
            Esta funcion sirve para guardar el path del archivo a contar
            resive el string del path 
            no regresa nada.
        """
        self.path=path

    def programaALineas(self):
        """

        """
        pass
    def conteoModificadas(self):
        """
        
        """
        pass
    def conteoBase(self):
        """
        
        """
        pass
    def limpiarLineas(self):
        """
        
        """
        pass
    def conteoTotal(self):
        """
        
        """
        pass
    def conteoAgregado(self):
        """
        
        """
        pass
    def filtradoAClases(self):
        """
        
        """
        pass
class Clase:
    arrLineasDelArchivo=[]

    def __init__(self,arr):
        """
            esta funcion es el constructor de la clase.
        """
        setArrLineasDelArchivo(arr)
        
    def setArrLineasDelArchivo(self,arr):
        """

        """
        self.arrLineasDelArchivo=arr

    def regresarCantidadDeFunciones(self):
        """

        """
        pass

    def regresarCantidadDeLineas(self):
        """

        """
        pass

    def conteoDeLineas(self):
        """

        """
        pass

    def conteoDeFunciones(self):
        """

        """
        pass