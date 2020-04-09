import math

def liczenie_promień(x, a, y, b):
    promien = math.sqrt(((x - a) ** 2) + ((y - b) ** 2))
    return promien
print("Promień tego koła wynosi:",(liczenie_promień(23,2,22,32)))