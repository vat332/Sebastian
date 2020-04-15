plik = open("Lekcja4/Do_zadania1.py","w+")

import random
from random import randint 
list = []
list = [random.randrange(0, 700, 4) for i in range(4)]
print(list)

plik.write(str(list))
plik.close()