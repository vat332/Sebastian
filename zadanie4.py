import math

def monotonicznosc_funkcji(a, x, b):
    y=(a*x)+b
    wynik = y
    if a==0:
        print("Funkcja stala")
    elif a<0:
        print("Funkcja malejaca")
    elif a>0:
        print("Funkcja rosnaca")
    else:
        print("Blad")
    return wynik
print(monotonicznosc_funkcji(-2, 3, 4))