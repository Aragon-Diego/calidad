"""
Numero de programa:06
Nombre:Diego Alonso Aragón Villarreal
Matricula:361349
Fecha ultima de modificación:17/04/2020
Razón de modificación:Creacion
"""
"""
Clases:
    EncontrarX
        setX
        encontrarX
        getX

"""
import p5 
import sys

class EncontrarX:
    x=0
    
    def setX(self,x):
        """
            La funcion recibe un valor de X
            y la guarda en la clase
        """
        self.x=x

    def encontrarX(self,p,x,dof):
        """
            Esta función es la funcion principal
            busca una x con una busqueda binaria
            regresa el valor de x encontrado
        """
        pasado = 0
        d=0.5
        while(True):
            clase=p5.Integrar(x,dof)
            pResultado=clase.regresarP()
            calculo=p-pResultado
            if(calculo<0):
                x-=d
            else:
                x+=d
            if(abs(calculo)<=0.000000000000001):
                break
            elif(not ((calculo<0) == (pasado<0))):
                d/=2
            pasado=calculo
        return round(x,5)

    def getX(self):
        """
            Regresa el valor encontrado de x
        """
        return self.x

    def __init__(self,p,dof,x):
        """
            Esta funcion es el constructor de la clase
        """
        self.setX(self.encontrarX(p,x,dof))

if __name__ == "__main__":
    try :
        p=float(sys.argv[1])
        if p > 1:
            raise ValueError('p invalido') 
        dof=float(sys.argv[2])
        x=1.0
        e=EncontrarX(p,dof,x)
        print(e.getX())
    except ValueError:
        print("hubo un error de entrada")