import numpy

def Liczonko(Wartosc , x):

    y = numpy.logspace(1,x,num=x,base=Wartosc,dtype='int')

    print(y)


Liczonko(2,4)
Liczonko(3,5)