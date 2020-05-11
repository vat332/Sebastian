import numpy


tablica2 = numpy.arange(12).reshape(3,4)
print(tablica2)


tablica3 = numpy.arange(12).reshape(4,3)
print(tablica3)


tablica4 = numpy.arange(12).reshape(2,6)
print(tablica4)


for a in tablica2.flat:
   print(a)
print("\n")


for a in tablica3.flat:
   print(a)
print("\n")


for a in tablica4.flat:
   print(a)