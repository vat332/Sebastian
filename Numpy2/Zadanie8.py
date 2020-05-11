import numpy


tablica = numpy.arange(9,18)
tablica = tablica.reshape(3, 3)


print(tablica)
y = 0
x = 0
while y < 3:
        print(tablica[x][y])
        y = y + 1
y=0
x=1
print("*****************")
while y < 3:
        print(tablica[x][y])
        y = y + 1
y=0
x=2
print("*******************")
while y < 3:
        print(tablica[x][y])
        y = y + 1