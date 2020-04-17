class slowa:

    def __init__(self, wyraz1, wyraz2):
        self.wyraz1 = wyraz1
        self.wyraz2 = wyraz2

    def sprawdz_czy_palindrom(self):
        odwrocone_slowo = reversed(self.wyraz1)
        odwrocone_slowo2 = reversed(self.wyraz2)
        if(list(self.wyraz1) == list(odwrocone_slowo)):
            print("slowo",self.wyraz1,"jest to palindrom")
        else:
           print("slowo",self.wyraz1,"nie jest palindromem")
        if(list(self.wyraz2) == list(odwrocone_slowo2)):
            print("slowo",self.wyraz2,"jest to palindrom")
        else:
           print("slowo",self.wyraz2,"nie jest palindromem")
    def sprawdz_czy_metagramy(self):
        y = 0
        pomoc = 0 
        x = len(self.wyraz1)
        while y < x:
            if self.wyraz1[y] != self.wyraz2[y]:
                pomoc = pomoc + 1
            y = y +1
        if pomoc > 1 :
            print("slowo",self.wyraz1,"i",self.wyraz2,"Nie sa metagrami")
        else:
            print("slowo",self.wyraz1,"i",self.wyraz2,"sa metagramami")
    def sprawdz_czy_anagramy(self):
        x = sorted(self.wyraz1)
        y = sorted(self.wyraz2)
        if(x == y):
            print("slowo",self.wyraz1,"i",self.wyraz2,"Sa anagramami")
        else:
            print("slowo",self.wyraz1,"i",self.wyraz2,"Nie sa to anagramy")
    def wyświetl_wyrazy(self):
        print("Pierwsze slowo:",self.wyraz1,"\nDrugie slowo:",self.wyraz2)          


pierwsze_slowo = slowa("mata", "tama")
pierwsze_slowo.sprawdz_czy_anagramy()
pierwsze_slowo.sprawdz_czy_palindrom()
pierwsze_slowo.wyświetl_wyrazy()
pierwsze_slowo.sprawdz_czy_metagramy()
