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
        setNombre
        regresarCantidadDeFunciones
        regresarCantidadDeLineas
        
"""
import sys
class Clase:
    arrLineasDelArchivo=[]
    nombre=""

    def setArrLineasDelArchivo(self,arr):
        """
            Esta funcion sirve para guardar el arreglo de lineas del archivo a contar
            resive el arreglo de string arr
            no regresa nada.
        """
        self.arrLineasDelArchivo=arr

    def setNombre(self,nombre):
        """
            Esta funcion sirve para guardar el nombre del archivo a contar
            resive el string con el nombre
            no regresa nada.
        """
        self.nombre=nombre[6:-2]

    def regresarCantidadDeFunciones(self):
        """
            esta fucnion hace el conteo de funciones
            regresa la cantidad de funciones en la clase
        """
        contador=0
        for linea in self.arrLineasDelArchivo:
            if "d"+"ef" in linea:
                contador+=1
        return contador

    def regresarCantidadDeLineas(self):
        """
            esta fucnion hace el conteo de lineas
            regresa la cantidad de lineas en la clase
        """
        contador=0
        for linea in self.arrLineasDelArchivo:
                if "#"+"Base" in linea or "#"+"Eliminado" in linea or  "#"+"Modificado" in linea:
                    continue
                contador+=1
        return contador

    def __init__(self,arregloDeClase):
        """
            esta funcion es el constructor de la clase.
        """
        self.setArrLineasDelArchivo(arregloDeClase)
        self.setNombre(self.arrLineasDelArchivo[0])
        


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
        clases=[]
        esClase=False
        i=-1
        for linea in self.arrLineasDelArchivo:
            if linea == 'if __name__ == "__main__":\n':
                esClase=False
                continue
            if "c"+"lass" in linea:
                esClase=True
                i+=1
                clases.append([linea])
                continue
            elif esClase:
                clases[i].append(linea)
                continue
        self.arrDeLineasPorClase=clases

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
        self.limpiarLineas()
        self.conteoTotal()
        self.conteoAgregado()
        self.filtradoAClases()
        for i in  range(len(self.arrDeLineasPorClase)): 
            self.clases.append(Clase(self.arrDeLineasPorClase[i]))
        
        

if __name__ == "__main__":
    path = str(sys.argv[1])
    programa=Programa(path)
    clases=programa.clases
    for clase in clases:
        print("Nombre: "+clase.nombre+" #Funciones: "+str(clase.regresarCantidadDeFunciones())+" #deLineas: "+str(clase.regresarCantidadDeLineas()))
    print("El total de lineas es: "+str(programa.total))
    print("El total de lineas agregadas fue: "+str(programa.agregadas))