import math#Para poder hacer raiz cuadrada
"""
clase lista dinamica
"""
class Lista:
    n=0
    lista=[]

    def agregar(self,num):#agrega un numero a la lista
        self.lista.append(num)
        self.n+=1

    def sumatoria(self):#hace una sumatroia de todos los numeros de la lista
        total=0
        for i in self.lista:
            total+=i
        return total

    def calMedia(self):#calcula media
        return (self.sumatoria()/self.n)

    def sumatoriaMedia(self):#hace la sumatoria de la media 
        total=0
        avg=self.calMedia()
        for i in self.lista:
            total+=(i-avg)**2
        return total

    def calDs(self):#calcula la desviacion estandar
        return math.sqrt(self.sumatoriaMedia()/(self.n-1))

"""
Programa
"""
l1=Lista()
with open("test2.txt",'r') as fp:#test.txt es el primer set de datos, test2.txt segundo set de datos
   num = fp.readlines()
   for i in num:
        l1.agregar(float(i))

print("Media:"+str(round(l1.calMedia(),2)))
print("des. Estandar:"+str(round(l1.calDs(),2)))