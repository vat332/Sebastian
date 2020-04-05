lista_zakupów = {"Chleb": 2,
         "Coca-Cola": 3,
         "Makaron": 4,
         "Ziemniaki": 5,
         "Czipsy": 3,
         "Mieszanka Wedlowska": 3,
         "Cytryna": 5,
         "Jablka": 5,
         "Piwo": 12,
         "Papierosy z kiosku": 10,
         "Gumy do zucia": 1}

def liczenie(** lista):
    print(sum(lista_zakupów.values()))
    
liczenie()
