import numpy


fibbonaci=numpy.array([1,1])

for Y in range(0,23):

    fibbonaci=numpy.append(fibbonaci,fibbonaci[-2]+fibbonaci[-1])
    A=numpy.array(fibbonaci)

A=A.reshape(5,5)

print(A)