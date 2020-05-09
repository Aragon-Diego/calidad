"""
Numero de programa:05
Nombre:Diego Alonso Aragón Villarreal
Matricula:361349
Fecha ultima de modificación:30/03/2020
Razón de modificación:Creacion
"""
"""
Clases:
    Integrar
        gama
        F
        sumaImpar
        sumaPar
        P
        chacarPs
"""
import math
import sys 
sys.setrecursionlimit(1500)
class Integrar:
    x=0
    dof=0
    p=0
    def gama(self,x):
        """
            Esta función es recursivo. Recibe un valor de X
            Y evalua el valor de su gama
            Regresa el valor de gama  
        """
        if x==1:
            return 1
        elif x == 0.5:
            return math.sqrt(math.pi)
        else:
            return (x-1)*self.gama(x-1)

    def F(self,x):
        """
            Recibe un valor de X
            Evalua la integral numéricamente 
            Regresa el calulo
        """
        return (self.gama((self.dof+1)/2)/((self.dof*math.pi)**(0.5)*self.gama(self.dof/2)))*((1+(x**2/self.dof))**(-1*((self.dof+1)/2)))

    def sumaImpar(self,numSeg,w):
        """
            Recibe el numero de segmentos y el valor de W
            Esta es la funcion de sumatoria para los numeros Impares
            Regresa el total de la sumatoria
        """
        total=0
        for i in range(1,numSeg,2):
            total+=4*self.F(i*w)
        return total

    def sumaPar(self,numSeg,w):
        """
            Recibe el numero de segmentos y el valor de W
            Esta es la funcion de sumatoria para los numeros Pares
            Regresa el total de la sumatoria
        """
        total=0
        for i in range(2,numSeg-1,2):
            total+=2*self.F(i*w)
        return total

    def P(self,x,numSeg):
        """
            Recibe el numero de segmentos, utiliza la x de la clase y tambien el dof
            Evalua la regla de Simpson  
            Regresa el calulo
        """
        w=x/numSeg
        return (w/3)*(self.F(0)+self.sumaImpar(numSeg,w)+self.sumaPar(numSeg,w)+self.F(x))

    def checarPs(self,p1,p2):
        """
            Esta funcion rescibe dos valores de P
            Evalua de forma booleana si el valor de la resta es menor que 0.00001
        """
        return abs(p1-p2) < 0.00001
    
    def regresarP(self):
        return self.p

    def __init__(self,x,dof):
        """
            Esta funcion es el constructor de la clase
        """
        self.x=x
        self.dof=dof
        numSeg=10
        p1=self.P(x,numSeg)
        p2=0
        while True:
            numSeg*=2
            p2=self.P(x,numSeg)
            if self.checarPs(p1,p2):
                break
            else:
                p1=p2
        self.p=p2

            
if __name__ == "__main__":
    x = float(sys.argv[1])
    dof = int(sys.argv[2])
    p=Integrar(x,dof)
    print(p)