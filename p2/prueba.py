"""
archivo=""
with open("../p1/p1.py",'r') as fp:#test.txt es el primer set de datos, test2.txt segundo set de datos
   archivo= fp.readlines()

print(archivo)
"""
import sys

def hello(a):
    print("hello and that's your sum:", a)

if __name__ == "__main__":
    a = int(sys.argv[1])
    hello(a)