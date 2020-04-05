import math

def arytmetyczny(a1, r, ile):
    suma = 0
    i = 0
    j = 1
    while i < ile:
        suma = suma + a1
        a1 = a1 + r
        i=i+1
        while j < ile:
            suma = suma*a1
            a1 = a1 + r
            suma2 = suma
            j=j+1
            print(suma2)
    return suma2

print(arytmetyczny(1,1,10))