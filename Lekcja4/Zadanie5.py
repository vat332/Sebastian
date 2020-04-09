class ciagi_arytmetyczne:
    #pierwszy_wyraz_ciagu = 231
    #różnica = 3
    #długość_ciągu = 123
    #Suma_ciągu = 1323

    def __init__(self, pierwszy_wyraz_ciagu, różnica, długość_ciągu, Suma_ciągu): #Działa
        self.pierwszy_wyraz_ciagu = pierwszy_wyraz_ciagu
        self.różnica = różnica
        self.długość_ciągu = długość_ciągu
        self.Suma_ciągu = Suma_ciągu

    def wyświetl_dane(self):
        print("Pierwszym elementym tego ciągu arytmetycznego jest ",self.pierwszy_wyraz_ciagu,"\nRożnica tego ciągu to :r =",self.różnica), #Działa
        print("Długość tego ciągu to:",self.długość_ciągu,"\nSuma tego ciągu o długości",self.długość_ciągu,"wynosi:S=",self.Suma_ciągu)
    
    def pobierz_parametry(self, pierwszy_wyraz_ciagu, różnica, długość_ciągu, Suma_ciągu):                          #Działa
        self.pierwszy_wyraz_ciagu = pierwszy_wyraz_ciagu
        self.różnica = różnica
        self.długość_ciągu = długość_ciągu
        self.Suma_ciągu = Suma_ciągu
    
    def pobierz_elementy(self, lista=[]):                                                           #chyba działa nwm jak to zrobic
        list = []
        print(lista)
    def policz_sume(self, pierwszy_wyraz_ciagu, różnica, długość_ciągu):
        self.Suma_ciągu = 0
        i = 0
        while i < self.długość_ciągu:
            self.Suma_ciągu = self.Suma_ciągu + self.pierwszy_wyraz_ciagu
            self.pierwszy_wyraz_ciagu = self.pierwszy_wyraz_ciagu + self.różnica
            i=i+1
        return self.Suma_ciągu

    def policz_elementy(self, pierwszy_wyraz_ciagu, różnica, Suma_ciągu):
        długość_ciągu = Suma_ciągu/różnica
        return długość_ciągu

ciag = ciagi_arytmetyczne(1,2,5,9)
ciag.wyświetl_dane()
print("\n")
ciag.pobierz_parametry(12,2,6,12)
ciag.wyświetl_dane()
ciag.pobierz_elementy([1,2,3,4,56,67,78,8,98])
ciag.pobierz_elementy()

#ciag = ciagi_arytmetyczne
#ciag.policz_sume(1,2,5)
#ciag3 = ciagi_arytmetyczne



