import numpy as np 
import pandas as pd 

dane = pd.read_excel("D:/Damian/python/KOLOSzPandasNumpyMatplotLIb/imiona.xlsx")

def zadanie1(dane):
    print(dane[dane['Liczba']>1000])

def zadanie2(dane):
    print(dane[dane['Imie']=="SEBASTIAN"])

def zadanie3(dane):
    liczbaUrodzen = dane['Liczba'].sum()
    print("Liczba urodzen: ", liczbaUrodzen)

def zadanie4(dane):
    przedzialLat = dane[(dane['Rok']>=2000) & (dane['Rok'] <=2005)]
    ilosc = przedzialLat['Liczba'].sum()
    print("Ilosc dzieci urodzony miedzy 2000-2005: ",ilosc)

def zadanie5(dane):
    M = dane.Liczba[dane.Plec == 'M']
    K = dane.Liczba[dane.Plec == 'K']
    print("Suma chlopcow: ",sum(M),"suma dziewczat:",sum(K))

def zadanie6(dane):
    print(dane.sort_values('Liczba',ascending=False).groupby(['Rok','Plec']).nth(0))
    
def zadanie7(dane):
    print(dane.sort_values('Liczba',ascending=False).groupby(['Plec']).head(1))
#zadanie1(dane)
#zadanie2(dane)
#zadanie3(dane)
#zadanie4(dane)
#zadanie5(dane)
#zadanie6(dane)
#zadanie7(dane)