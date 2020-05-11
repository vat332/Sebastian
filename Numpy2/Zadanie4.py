import numpy

tablica = numpy.arange(3)
tablica = tablica.reshape(1, 3)
print(tablica)


tablica2 = numpy.arange(3,4.5,0.5)
tablica2 = tablica2.reshape(1, 3)
print(tablica2)


tablica = tablica*tablica2
print(tablica)