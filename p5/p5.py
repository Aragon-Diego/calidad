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
"""
import math
import sys 

class Integrar:
    x=0
    dof=0

    def gama(self,x):
        """

        """
        if x==1:
            return 1
        elif x == 0.5:
            return math.sqrt(math.pi)
        else:
            return (x-1)*self.gama(x-1)

    def F(self,x):
        """

        """
        return (self.gama((self.dof+1)/2)/((self.dof*math.pi)**(0.5)*self.gama(self.dof/2)))*((1+(x**2/self.dof))**(-1*((self.dof+1)/2)))

    def suma1(self,numSeg,w):
        """
        
        """
        total=0
        for i in range(1,numSeg,2):
            total+=4*self.F(i*w)
        return total

    def suma2(self,numSeg,w):
        """

        """
        total=0
        for i in range(2,numSeg-1,2):
            total+=2*self.F(i*w)
        return total

    def P(self,numSeg):
        """

        """
        w=self.x/numSeg
        return (w/3)*(self.F(0)+self.suma1(numSeg,w)+self.suma2(numSeg,w)+self.F(self.x))

    def checarPs(self,p1,p2):
        """

        """
        return abs(p1-p2) < 0.00001

    def __init__(self,x,dof):
        """

        """
        self.x=x
        self.dof=dof
        numSeg=10
        p1=self.P(numSeg)
        p2=0
        while True:
            numSeg*=2
            p2=self.P(numSeg)
            if self.checarPs(p1,p2):
                break
            else:
                p1=p2
        print(round(p2,5))
            
if __name__ == "__main__":
    x = float(sys.argv[1])
    dof = int(sys.argv[2])
    Integrar(x,dof)