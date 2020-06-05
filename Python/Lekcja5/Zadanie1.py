class Material:
    def __init__(self, nazwa, rodzaj, długość, szerokość):
       self.rodzaj = rodzaj
       self.długość = długość
       self.szerokość = szerokość
       self.nazwa = nazwa

    def wyswietl_nazwe(self):
        return print(self.nazwa)

class Ubrania(Material):
    def __init__(self, rozmiar, kolor, dla_kogo):
        self.rozmiar = rozmiar
        self.kolor = kolor
        self.dla_kogo = dla_kogo

    def wyświetl_dane(self):
        return print("\nRozmiar:",self.rozmiar,"\nKolor:",self.kolor,"\nDla kogo:",self.dla_kogo)

class Sweter(Ubrania):
    def __init__(self, rodzaj_swetra):
        self.rodzaj_swetra = rodzaj_swetra
    
    def wyświetl_dane(self):
        return print("Atrybuty przedmiotu:",self.rodzaj_swetra)

Produkt1 = Material("Koszula","Elegancka",140,80)
Produkt1.wyswietl_nazwe()
Produkt1 = Ubrania("L","czerowny","kobieta")
Produkt1.wyświetl_dane()
Produkt1 = Sweter("Z guzikami")
Produkt1.wyświetl_dane()
