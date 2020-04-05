import math

def arytmetyczny(a1, r, ile):
    suma = 0
    i = 0
    while i < ile:
        suma = suma + a1
        a1 = a1 + r
        i=i+1
    return suma

print(arytmetyczny(1,1,10))