import numpy

def dodawanie(a, b):
    c = 0
    c = a + b
    print(c)


tablica = numpy.arange(6)
tablica = tablica.reshape(2, 3)
print(tablica)


tablica2 = numpy.arange(6, 12)
tablica2 = tablica2.reshape(2, 3)
print(tablica2)


dodawanie(tablica,tablica2)
