import numpy


def Liczenie(n):

    Macierz = numpy.arange(1,(n*n)+1,1)
    Macierz = Macierz.reshape(n, n)

    print(Macierz)


Liczenie(9)
Liczenie(2)
    
    