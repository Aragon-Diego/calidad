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
            Esta funcion toma el archivo a contar y lo guarda en un arreglo
            no regresa nada
        """
        pass
    def conteoModificadas(self):
        """
            Esta funcion es la que cuenta la cantidad de lineas modificadas
            no regresa nada
        """
        pass
    def conteoBase(self):
        """
            Esta funcion es la que cuenta la cantidad de lineas base
            no regresa nada
        """
        pass
    def limpiarLineas(self):
        """
            Esta funcion lipia el arreglo con las lineas de codigo
            quitando los comentarios 
            no regresa nada
        """
        pass
    def conteoTotal(self):
        """
            cuenta la cantidad de lineas del arreglo con las reglas de conteo
            no reresa nada
        """
        pass
    def conteoAgregado(self):
        """
            esta funcion cuenta la cantidad de lineas agregadas en el codigo
            suma la cantidad de codigo base + codigo modificado y se lo resta al total
            no regresa nada
        """
        pass
    def filtradoAClases(self):
        """
            esta funcion es la que toma el arreglo de lineas y lo separa por clases
            no regresa nada
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
            Esta funcion sirve para guardar el arreglo de lineas del archivo a contar
            resive el arreglo de string arr
            no regresa nada.
        """
        self.arrLineasDelArchivo=arr

    def regresarCantidadDeFunciones(self):
        """
            esta fucnion hace el conteo de funciones
            regresa la cantidad de funciones en la clase
        """
        pass

    def regresarCantidadDeLineas(self):
        """
            esta fucnion hace el conteo de lineas
            regresa la cantidad de lineas en la clase
        """
        pass
