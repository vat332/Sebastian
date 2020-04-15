class robaczek:

    def __init__(self, x, y, krok):
        self.x = x
        self.y = y
        self.krok = krok
    def idz_w_gore(self, ile_krokow):
        self.y = self.y+ ile_krokow*self.krok
    def idz_w_dol(self, ile_krokow):
        self.y = self.y - ile_krokow*self.krok
    def idz_w_lewo(self, ile_krokow):
        self.x = self.x - ile_krokow*self.krok
    def idz_w_prawo(self, ile_krokow):
        self.x = self.x + ile_krokow*self.krok
    def pokaz_gdzie_jestes(self):
        print(self.x, self.y)
    def __del__(self):
        print("usunieto",self)

szczur = robaczek(0,0,1)
szczur.idz_w_gore(5)
szczur.idz_w_dol(5)
szczur.idz_w_lewo(233)
szczur.idz_w_prawo(123)
szczur.pokaz_gdzie_jestes()
szczur.__del__()