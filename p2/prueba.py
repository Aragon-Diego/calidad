archivo=""
with open("../p1/p1.py",'r') as fp:#test.txt es el primer set de datos, test2.txt segundo set de datos
   archivo= fp.readlines()

print(archivo)