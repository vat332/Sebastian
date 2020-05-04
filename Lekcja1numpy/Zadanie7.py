import numpy

def funkcja(n):
    Pierwsze=numpy.zeros((n,n))

    x=1
    y=2

    while y<n:  #dolna czesc macierzy
        Pierwsze=Pierwsze+numpy.diag(numpy.full(n-x,2*y),-x)

        x=x+1
        y=y+1

    x=0
    y=1

    while x<n:      #Górna czesc macierzy
        Pierwsze=Pierwsze+numpy.diag(numpy.full(n-x,2*y),x)

        x=x+1
        y=y+1

    print(Pierwsze)


funkcja(3)
