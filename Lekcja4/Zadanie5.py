class ciagi_arytemtyczne:
    def __init__(self, pierwszy_wyraz_ciagu, różnica, długość_ciągu, Suma_ciągu): #Działa
        self.pierwszy_wyraz_ciagu = pierwszy_wyraz_ciagu
        self.różnica = różnica
        self.długość_ciągu = długość_ciągu
        self.Suma_ciągu = Suma_ciągu
    def wyświtel_dane(self):
        print("Pierwszym elementym tego ciągu arytmetycznego jest ",self.pierwszy_wyraz_ciagu,"\nRożnica tego ciągu to :r =",self.różnica), #Działa
        print("Długość tego ciągu to:",self.długość_ciągu,"\nSuma tego ciągu o długości",self.długość_ciągu,"wynosi:S=",self.Suma_ciągu)
    def pobierz_elementy(self):
        x = input("Podaj elementy ciagu:")
        print(x)
    def pobierz_parametry(self, pierwszy_wyraz_ciagu, różnica, długość_ciągu):                          #Działa
        self.pierwszy_wyraz_ciagu = pierwszy_wyraz_ciagu
        self.różnica = różnica
        self.długość_ciągu = długość_ciągu
        licznik = 1
        an = 0
        while licznik <= self.długość_ciągu:
            an = self.pierwszy_wyraz_ciagu + (licznik - 1) * self.różnica
            print(an)
            licznik += 1
    def policz_sume(self , pierwszy_wyraz_ciagu , różnica , długość_ciągu):
        self.pierwszy_wyraz_ciagu = pierwszy_wyraz_ciagu
        self.różnica = różnica
        self.długość_ciągu = długość_ciągu
        Suma_ciągu = 0
        i = 0
        an = 0
        licznik = 1
        while licznik <= self.długość_ciągu:
            an = self.pierwszy_wyraz_ciagu + (licznik - 1) * self.różnica
            licznik += 1
        Suma_ciągu =((self.pierwszy_wyraz_ciagu + an) / 2) * self.długość_ciągu
        print("\n\n",an)
        print(licznik)
        print(Suma_ciągu,"essa")
    def policz_elementy(self, pierwszy_wyraz_ciagu, różnica, Suma_ciągu):
        self.pierwszy_wyraz_ciagu = pierwszy_wyraz_ciagu
        self.różnica = różnica
        długość_ciągu = Suma_ciągu/różnica
        print(długość_ciągu)

ciag1 = ciagi_arytemtyczne(1, 2 , 15 ,500)
#ciag1.pobierz_elementy()
ciag1.pobierz_parametry(1,2,10)
ciag1.policz_sume(1,4,10)
ciag1.policz_elementy(1,2,100)