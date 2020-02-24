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
        multiplicarArreglos
        alCuadradoArreglo
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
        arreglo=[]
        with open(nombreDeArchivo) as f:
            arreglo = f.readlines()
        arreglo = [x.strip() for x in arreglo]
        arreglo = [float(x) for x in arreglo] 
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

    def multiplicarArreglos(self,arreglo1,arreglo2):
        """
            Esta funcion resive dos arreglos de numeros y regresa un arreglo nuevo 
            con el resultado de multiplicar cada elemento por su respectivo del otro arreglo
            multiplicacion = arreglo1[0]*arreglo2[0]
        """
        arreloResultante=[]
        for i in range(len(arreglo1)):
            arreloResultante.append(arreglo1[i]*arreglo2[i])
        return arreloResultante

    def alCuadradoArreglo(self,arreglo):
        """
            Esta funcion resive un arreglo de numeros 
            regresa un arreglo nuevo con cada elemento del arreglo anterior
            multiplicado por si mismo
        """
        arreloResultante=[]
        for num in arreglo:
            arreloResultante.append(num**2)
        return arreloResultante

    def calculaB1(self):
        """
            Esta funcion calcula la b1 de dos sets de numeros
            al terminar guarda el resultado en la variable global b1
        """
        self.b1=((self.sumatoria(self.multiplicarArreglos(self.xs,self.ys)))-(len(self.xs)*self.promedio(self.xs)*self.promedio(self.ys)))/((self.sumatoria(self.alCuadradoArreglo(self.xs)))-(len(self.xs)*(self.promedio(self.xs)**2)))

    def calculaB0(self):
        """
            Esta funcion calcula la b0 de dos sets de numeros
            al terminar guarda el resultado en la variable global b0
        """
        self.b0=self.promedio(self.ys)-(self.b1*self.promedio(self.xs))

    def calculaR(self):
        """
            Esta funcion calcula la r de dos sets de numeros
            al terminar guarda el resultado en la variable global r
        """
        self.r=((len(self.xs)*self.sumatoria(self.multiplicarArreglos(self.xs,self.ys)))-(self.sumatoria(self.xs)*self.sumatoria(self.ys)))/(math.sqrt(abs((len(self.xs)*self.sumatoria(self.alCuadradoArreglo(self.xs))-(self.sumatoria(self.xs)**2))*(len(self.ys)*self.sumatoria(self.alCuadradoArreglo(self.ys))-(self.sumatoria(self.ys)**2)))))
        
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
        rCuadrada=self.calculaRCuadrada()
        print("B0: "+str(round(self.b0,4))+", B1: "+str(round(self.b1,4))+", r: "+str(round(self.r,4))+", r^2: "+str(round(rCuadrada,4))+", Yk: "+str(round(self.yResultante,4)))
        if(rCuadrada>=0.9):
            print("the relationship is predictive; use it with high confidence")
        elif(rCuadrada>=0.7):
            print("the relationship is strong and can be used for planning")
        elif(rCuadrada>=0.5):
            print("the relationship is adequate for planning but use with caution")
        else:
            print("the relationship is not reliable for planning purposes")

    def setXs(self,arreglo):
        """
            Esta funcion resive un arreglo y lo guarda en la variable global
            xs
        """
        self.xs=arreglo

    def setYs(self,arreglo):
        """
            Esta funcion resive un arreglo y lo guarda en la variable global
            ys
        """
        self.ys=arreglo

    def setXK(self,xK):
        """
            Esta funcion resive un numero entero y lo guarda en la variable global
            xK
        """
        self.xK=xK

    def __init__(self,archivoX,archivoY,xK=386):
        """
            Esta funcion es el constructor de la clase
        """
        self.setXs(self.archivoAArreglo(archivoX))
        self.setYs(self.archivoAArreglo(archivoY))
        self.setXK(xK)
        self.calcularYResultante()
        self.calculaR()
        

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
        print("_________________________")
        print("estimado #"+str(contador)+" ",end="")
        estimado.imprimir()
        print("_________________________")