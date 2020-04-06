class PierwszaKlasa:
    """Przykład klasy"""
    atrybut = 54321

    def pierwsza_metoda(self, z): #self kopiuje i nastepnie robi
        return "Teraz działa pierwsza Metoda"

obiekt = PierwszaKlasa()
print(obiekt)
print(isinstance(obiekt, object)) #Sprawdzanie typu zmiennej (nazwa, jaki typ sprawdzic)
print(obiekt.atrybut)
print(obiekt.pierwsza_metoda(3))
#<__main__.PierwszaKlasa object at 0x00A17178>
#True
obiekt.tekst = "la la la"
print(obiekt.tekst)

class Osoba:
    pass

marek = Osoba()
marek.imie = 'Marek'
marek.nazwisko = 'Kamiński'

print(marek.__dict__) #dict zwraca w formie słownika 
#{'imie': 'Marek', 'nazwisko': 'Kamiński'}

karol = Osoba()
karol.imie = 'Karol'
karol.nazwisko = 'Siemaszko'

#__del__(self) jest wywolane kiedy klasa jest usuwana np. obiekt z pamieci, ale najczesciej robi sie to samo poporzez garbage collector.


