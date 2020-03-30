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
            Esta funcion es llamada con un arreglo como parametro
            Utiliza la funcion sum() de python para hacer la sumatoria de cada elemento 
            regresa la sumatoria calculada
        """
        return sum(arr)

    def promedio(self,arr):
        """
            Esta funcion es llamada con un arreglo como parametro 
            regresa el promedio del arreglo como un numero flotante
        """
        return sum(arr)/len(arr)

    def archivoAArreglo(self,archivo):
        """
            Esta funcion es llamada con un string como parametro
            el string tiene que tener un path de un archivo con datos
            la informacion del arreglo es guardado en la variable global  
            setDeDatos
        """
        arreglo=[]
        archivo=open(archivo)
        with archivo as f:
            arreglo=f.readlines()
        arreglo=[ (float(numeros.split(",")[0])/float(numeros.split(",")[1])) for numeros in arreglo]
        self.setDeDatos=arreglo
        
    def arregloALn(self):
        """
            Esta funcion toma el set de datos de la variable global setDeDatos
            y a cada uno de sus elementos le hace un logaritmo natural y lo 
            adjunta a la variable global setDeLn
        """
        self.setDeLn=[math.log(numero) for numero in self.setDeDatos]
        
    def calcularVariante(self):
        """
            Esta funcion toma los datos de la variable global setDeLn
            y calcula su variante
            regresa la variante
        """
        promedio=self.promedio(self.setDeLn)
        arreglo=[((dato-promedio)**2) for dato in self.setDeLn]
        return (self.sumatoria(arreglo)/(len(arreglo)-1))
        
    def calcularDesviacionEstandar(self):
        """
            Esta funcion calcula la desviacion estandar
            regresa la desviavcion estandar
        """
        return math.sqrt(self.calcularVariante())

    def calcularResultadosLogaritmoNatural(self):
        """
            Esta funcion calcula los resultados de vs, s , m , l , vl
            de logaritmo natural.
            los resultados los guara en la variable global setDeResultados
        """
        arrDeResultados=[]
        desviacionEstandar=self.calcularDesviacionEstandar()
        promedio=self.promedio(self.setDeLn)
        for i in range(-2,3):
            arrDeResultados.append(promedio+(i*desviacionEstandar))
        self.setDeResultados=arrDeResultados

    def calcularResultados(self):
        """
            Esta funcion toma cada elemento del arreglo setDeResultados
            y lo transforma haciendo con un exponencial
        """
        self.setDeResultados=[math.exp(numero) for numero in self.setDeResultados]
    
    def imprimir(self):
        """
            Esta funcion se encarga de imprimir los datos de la clase
        """
        arregloDeStrings=['VS','S','M','L','VL']
        for i in range(len(arregloDeStrings)):
            print(arregloDeStrings[i]+":"+str(round(self.setDeResultados[i],4)),end=" ")
        print("")

    def __init__(self,archivo):
        """
            Esta funcion es el constructor de la clase
        """
        self.archivoAArreglo(archivo)
        self.arregloALn()
        self.calcularDesviacionEstandar()
        self.calcularResultadosLogaritmoNatural()
        self.calcularResultados()
        self.imprimir()

if __name__ == "__main__":
    archivo = str(sys.argv[1])
    Rangos(archivo)