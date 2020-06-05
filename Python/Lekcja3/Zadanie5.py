import math

def rownolegle_czy_prostopadle(a1 = 0, b1 = 0, a2 = 0, b2 = 0, x = 0):
    y=a1*x+b1
    y2=a2*x+b2
    wynik1=y
    wynik2=y2
    wynik=a1+a2
    if a1==a2:
        print("Są rownoległe")
    elif wynik == -1:
        print("Są prostopadłe")
    else:
        print("Nie można określić monotonicznośći")
    return wynik1, wynik2
print(rownolegle_czy_prostopadle(1,2,-2,3,4))
print(rownolegle_czy_prostopadle(1,2,1,-2,3))
print(rownolegle_czy_prostopadle(1,1,3,1,3))