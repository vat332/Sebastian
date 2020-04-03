[print(f"liczba: {x}") for x in range(5)]



slownik = {'imie': 'Adam', 'wiek': 25}
for klucz in slownik: #klucz
    print(slownik[klucz])

print(slownik.items())

krotka = tuple()
krotka = ()
zbior = set()
zbior = {2, 3, 4, 5}

#lista krotek



lista = [('imie', 'adam'), ('wiek', 25)]

imie = lista[0][1]
wiek = lista[1][1]

etykieta, wartosc = lista[0]

for cos, cos2 in slownik.items():
    print(cos, cos2)

slownik = {'imie': 'Adam', 'wiek': 25}

slownik2 = {str(x):x for x in range(10)}
slownik2 = {wartosc: klucz for klucz, wartosc in slownik.items()}
print(slownik2)
