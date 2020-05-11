import numpy 

tablica = numpy.arange(9)
tablica = tablica.reshape(3, 3)
print(tablica)


tablica2 = numpy.arange(16)
tablica2 = tablica2.reshape(4, 4)
print(b)


print(tablica2.min(axis=0))
print("\n")
print(tablica2.min(axis=1))
print("\n")
print(tablica.min(axis=0))
print("\n")
print(tablica.min(axis=1))