import numpy

def DzielenieMacierzy(Macierz,kierunekPionPoziom):
    print(Macierz)
    if kierunekPionPoziom == 1:
        if Macierz.shape[0] %2==0:

            x = Macierz.shape[0] / 2
            x = int(x)
            print('\n')
            print(Macierz[0:x],"\n")
            print(Macierz[x:])

        if Macierz.shape[0] %2==1:

            print("Nie mozna podzielic ze wzgledu na wiesze!!!!!")

    if kierunekPionPoziom == 0:
        if Macierz.shape[1] %2==0:

            x = Macierz.shape[1] / 2
            x = int(x)
            print('\n')
            print(Macierz[:,0:x],"\n")
            print(Macierz[:,x:])

        if Macierz.shape[1] %2==1:

            print("Nie mozna podzielic ze wzgledu na kolumny!!!!!")            


Macierz = numpy.arange(36).reshape((6,6))


DzielenieMacierzy(Macierz, 1)
