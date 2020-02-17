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
        conteoEliminadas
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
    eliminado=0
    path=""
    arrLineasDelArchivo=[]
    arrDeLineasPorClase=[]

    def filtradoAClases(self):
        """
            esta funcion es la que toma el arreglo de lineas y lo separa por clases
            no regresa nada
        """
        pass

    def conteoAgregado(self):
        """
            esta funcion cuenta la cantidad de lineas agregadas en el codigo
            suma la cantidad de codigo base + codigo modificado + codigo eliminado y se lo resta al total
            no regresa nada
        """
        self.agregadas=self.total-(self.eliminado+self.modificadas+self.base)

    def conteoTotal(self):
        """
            cuenta la cantidad de lineas del arreglo con las reglas de conteo
            no reresa nada
        """
        for linea in self.arrLineasDelArchivo:
            if not linea  == "\n":
                self.total+=1
    
    def limpiarLineas(self):
        """
            Esta funcion lipia el arreglo con las lineas de codigo
            quitando los comentarios 
            no regresa nada
        """
        arrLimpio=[]
        tripeComilla=False
        for linea in self.arrLineasDelArchivo:
            if  '"""\n' in linea:
                tripeComilla = not  tripeComilla
                continue
            if tripeComilla:
                continue
            else:
                if "if" in linea:
                    arrLimpio.append(linea)
                    continue
                elif  "#" in linea or linea == "\n":
                    continue
                else:
                    arrLimpio.append(linea)
                    continue
        self.arrLineasDelArchivo=arrLimpio

    def conteoEliminadas(self):
        """
            Esta funcion es la que cuenta la cantidad de lineas eliminadas
            no regresa nada
        """
        for linea in self.arrLineasDelArchivo:
            if  "#"+"Eliminado" in linea:
                self.eliminado+=1

    def conteoBase(self):
        """
            Esta funcion es la que cuenta la cantidad de lineas base
            no regresa nada
        """
        for linea in self.arrLineasDelArchivo:
            if  "#"+"Base" in linea:
                self.base+=1
    
    def conteoModificadas(self):
        """
            Esta funcion es la que cuenta la cantidad de lineas modificadas
            no regresa nada
        """
        for linea in self.arrLineasDelArchivo:
            if  "#"+"Modificado" in linea:
                self.modificadas+=1

    def programaALineas(self):
        """
            Esta funcion toma el archivo a contar y lo guarda en un arreglo
            no regresa nada
        """
        with open(self.path,'r') as fp:#test.txt es el primer set de datos, test2.txt segundo set de datos
            self.arrLineasDelArchivo= fp.readlines()
        
        
    def setPath(self,path):
        """
            Esta funcion sirve para guardar el path del archivo a contar
            resive el string del path 
            no regresa nada.
        """
        self.path=path

    def __init__(self,path):
        """
            esta funcion es el constructor de la clase.
        """
        self.setPath(path)
        self.programaALineas()
        self.conteoModificadas()
        self.conteoBase()
        self.conteoEliminadas()
        #print("mod:",self.modificadas) 
        #print("base:",self.base) 
        #print("elim:",self.eliminado) 
        self.limpiarLineas()
        self.conteoTotal()
        print("total:",self.total)
        self.conteoAgregado()
        print("agre:",self.agregadas)
        #self.filtradoAClases()
        #for arregloDeClase in  arrDeLineasPorClase: clase=Clase(arregloDeClase)


class Clase:
    arrLineasDelArchivo=[]
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

    def __init__(self,arregloDeClase):
        """
            esta funcion es el constructor de la clase.
        """
        self.setArrLineasDelArchivo(arregloDeClase)

if __name__ == "__main__":
    path = str(sys.argv[1])
    programa=Programa(path)
