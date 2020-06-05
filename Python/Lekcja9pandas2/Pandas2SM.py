import numpy as np 
import pandas as pd 

url = "https://raw.githubusercontent.com/kropiak/wd/master/8_pandas_1/datasets/zamowienia.csv"

dane = pd.read_csv(url, "error_bad_lines=False",delimiter=";")

def zadanie1(dane):
    print(dane['Sprzedawca'].unique())

def zadanie2(dane):
    print(dane.sort_values(['Utarg'],ascending=False).head(5))

def zadanie3(dane):
    print(dane.groupby('Sprzedawca').count())

def zadanie4(dane):
    x = dane.groupby('Kraj').count()
    print(x['idZamowienia'])

def zadanie5(dane):
    liczba = dane[(dane['Kraj']=='Polska') & (dane['Data zamowienia'] >= '2005-01-01') & (dane['Data zamowienia'] <= '2006-01-01')].count()
    print("Ilosc zamowien:",liczba['idZamowienia'])

def zadanie6(dane):
    srednia = dane[(dane['Data zamowienia']>='2004-01-01') & (dane['Data zamowienia']<='2005-01-01')]
    srednia2 = srednia['Utarg'].mean()
    print(srednia2)
def zadanie7(dane):
    rok2005=dane[(dane['Kraj']=='Polska') & (dane['Data zamowienia']>='2005-01-01')& (dane['Data zamowienia']<'2006-01-01')]
    print(rok2005)
    rok2005.to_csv('D:/Damian/python/KOLOSzPandasNumpyMatplotLIb/zamowieniaSM_2005.csv')

    rok2004=dane[(dane['Kraj']=='Polska') & (dane['Data zamowienia']>='2005-01-01')& (dane['Data zamowienia']<'2006-01-01')]
    print(rok2004)
    rok2004.to_csv('D:/Damian/python/KOLOSzPandasNumpyMatplotLIb/zamowieniaSM_2004.csv')
#zadanie1(dane)
#zadanie2(dane)
#zadanie3(dane)
#zadanie4(dane)
#zadanie5(dane)
#zadanie6(dane)
#zadanie7(dane)