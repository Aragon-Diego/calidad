"""
Numero de programa:07
Nombre:Diego Alonso Aragón Villarreal
Matricula:361349
Fecha ultima de modificación:09/05/2020
Razón de modificación:Creacion
"""
"""
Clases:
    

"""
import p3 
import p5 
import p6
import sys
import math
class Programa7:
    xs=[]
    ys=[]
    b0=0
    b1=0
    r=0
    r2=0
    y=0
    x=0
    nDatos=0
    p=0
    tail=0
    desvEst=0
    rango=0
    xk=0
    upi=0
    lpi=0
    def sumatoria2(self):
        """

        """
        count=0
        for i in range(len(self.xs)):
            count+=(self.xs[i]-(sum(self.xs)/len(self.xs)))**2
        return count
    def sumatoria(self):
        """

        """
        count=0
        for i in range(len(self.xs)):
            count+=(self.ys[i]-self.b0-(self.b1*self.xs[i]))**2
        return count
    def divisionEstandar(self):
        """

        """
        self.desvEst=math.sqrt((1/(self.nDatos-2))*self.sumatoria()) 
    def calcularRango(self):
        """

        """
        t=p6.EncontrarX(0.35,self.nDatos-2,1)
        x=t.getX()
        self.divisionEstandar()
        derecha=math.sqrt(abs(1+(1/self.nDatos)+((self.xk-(sum(self.xs)/len(self.xs)))**2/(self.sumatoria2()))))
        self.rango=x*self.desvEst*derecha
    def calcularTail(self):
        """

        """
        self.tail=1-(2*self.p)
    def calcularP(self):
        """
        
        """
        integrar=p5.Integrar(self.x,self.nDatos-2)
        self.p=integrar.p
    def calcularX(self):
        """

        """
        self.x=((abs(self.r)*math.sqrt(self.nDatos-2))/(math.sqrt(1-self.r2)))
    def __init__(self,b0,b1,r,r2,y,nDatos,xs,ys,xk):
        """

        """
        self.xk=xk
        self.xs=xs
        self.ys=ys
        self.b0=b0
        self.b1=b1
        self.r=r
        self.r2=r2
        self.y=y
        self.nDatos=nDatos
        self.calcularX()
        self.calcularP()
        self.calcularTail()
        self.calcularRango()
        self.upi=self.y+self.rango
        self.lpi=self.y-self.rango

if __name__ == "__main__":
    xk=float(sys.argv[3])
    estimar = p3.Estimador(str(sys.argv[1]),str(sys.argv[2]),xk)
    p7= Programa7(estimar.b0,estimar.b1,estimar.r,estimar.r2,estimar.yResultante,len(estimar.xs),estimar.xs,estimar.ys,xk)
    print("rxy= "+str(round(p7.r,9))+"\nr**2= "+str(round(p7.r2,9))+"\ntail= "+str(round(p7.tail,9))+"\nb0= "+str(round(p7.b0,9))+"\nb1= "+str(round(p7.b1,9))+"\nyk= "+str(round(p7.y,9))+"\nRange= "+str(round(p7.rango,9))+"\nupi= "+str(round(p7.upi,9))+"\nlpi= "+str(round(p7.lpi,9)),end="")