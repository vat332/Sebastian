import random
from random import randint 
macierz = [
    [1, 2, 3, 1],
    [4, 5, 6, 2],
    [7, 8, 9, 3],
    [1, 3, 5, 1]
]
x = 0
y = 0
while y < 4:
    print(macierz[y][y])
    y +=1

#for rzad in macierz:
 #   for xd in rzad:
  #      if()

#plaska = [x for poziomo in macierz for x in poziomo]
#print(plaska)

N = 4
list2 = [[random.randrange(-10, 10, 1) for i in range(4)] for j in range(4)]
print(list2)
print("liczby z przekatnej:\n")
przekatna = [rzad[y] for y,rzad in enumerate(list2)]
print(przekatna)