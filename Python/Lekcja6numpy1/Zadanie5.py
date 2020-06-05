import numpy


def Wektor(n):

    Pierwsze = numpy.arange(n, 0,-1)
    print(Pierwsze)
    print('\n')
    Drugie = numpy.diag(Pierwsze)
    print(Drugie)
    print('\n')

Wektor(3)
Wektor(4)
Wektor(5)