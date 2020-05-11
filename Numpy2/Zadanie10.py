import numpy


tablica2 = numpy.arange(81).reshape(9,9)
print(tablica2)


tablica2 = tablica2.reshape(1,81)
print(tablica2)


tablica2 = tablica2.reshape(81,1)
print(tablica2)

