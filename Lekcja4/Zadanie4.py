class Na_zakupy:
    waluta = "zł"
    
    def __init__(self, nazwa_produktu, ilosc, jednosta_miary, cena_jed):
        self.nazwa_produktu = nazwa_produktu
        self.ilosc = ilosc
        self.jednosta_miary = jednosta_miary
        self.cena_jed = cena_jed
    
    def wyświetl_produkt(self):
        print("Nazwa produktu",self.nazwa_produktu,"\nIle sztuk:",self.ilosc,"\nJednostka miary:",self.jednosta_miary,"\nCena za sztuke:", self.cena_jed,self.waluta)
    def ile_produktu(self):
        print(self.nazwa_produktu,"jest:",self.ilosc,self.jednosta_miary)
    def ile_kosztuje(self):
        cena = 0
        cena = self.ilosc*self.cena_jed
        #return self.nazwa_produktu, cena, self.jednosta_miary
        print("Za",self.ilosc,self.jednosta_miary,self.nazwa_produktu,"trzeba zapłacić",cena,self.waluta)

coca_cola = Na_zakupy("Coca-cola", 6, "butelki", 5)
ziemniaki = Na_zakupy("Ziemniaki", 123, "kg", 3.2)
mieso = Na_zakupy("Mieso", 12, "kg", 4)
alkohol = Na_zakupy("Alokohol", 3, "butelki", 50)

alkohol.ile_kosztuje()
alkohol.ile_produktu()
coca_cola.ile_produktu()
coca_cola.ile_kosztuje()
alkohol.wyświetl_produkt()
#print(ziemniaki.ile_kosztuje("ziemniaki", 12, 2.4, "kg"))
#ziemniaki.ile_kosztuje()