class slowa:

    def __init__(self, slowo1, slowo2):
        self.slowo1 = slowo1
        self.slowo2 = slowo2

    def sprawdz_czy_palindrom(self):
        odwrocone_slowo = reversed(self.slowo1)
        odwrocone_slowo2 = reversed(self.slowo2)
        if(list(self.slowo1) == list(odwrocone_slowo)):
            print("slowo",self.slowo1,"jest to palindrom")
        else:
           print("slowo",self.slowo1,"nie jest palindromem")
        if(list(self.slowo2) == list(odwrocone_slowo2)):
            print("slowo",self.slowo2,"jest to palindrom")
        else:
           print("slowo",self.slowo2,"nie jest palindromem")
    def sprawdz_czy_metagramy(self):
        licznik = 0 
        z = 0
        x = len(self.slowo1)
        while z < x:
            if self.slowo1[z] != self.slowo2[z]:
                licznik = licznik + 1
            z = z +1
        if licznik > 1 :
            print("slowo",self.slowo1,"i",self.slowo2,"Nie sa metagrami")
        else:
            print("slowo",self.slowo1,"i",self.slowo2,"sa metagramami")
    def sprawdz_czy_anagramy(self):
        x = sorted(self.slowo1)
        y = sorted(self.slowo2)
        if(x == y):
            print("slowo",self.slowo1,"i",self.slowo2,"Sa anagramami")
        else:
            print("slowo",self.slowo1,"i",self.slowo2,"Nie sa to anagramy")
    def wyświetl_wyrazy(self):
        print("Pierwsze slowo:",self.slowo1,"\nDrugie slowo:",self.slowo2)          


pierwsze_slowo = slowa("mata", "tama")
pierwsze_slowo.sprawdz_czy_palindrom()
pierwsze_slowo.sprawdz_czy_metagramy()
pierwsze_slowo.sprawdz_czy_anagramy()
pierwsze_slowo.wyświetl_wyrazy()
