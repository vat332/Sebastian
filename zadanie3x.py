skroty = {"Chleb": "sztuki",
         "Coca-Cola": "sztuki",
         "Makaron": "sztuki",
         "Ziemniaki": "kilogramy",
         "Czipsy": "opakowania",
         "Mieszanka Wedlowska": "kilogramy",
         "Cytryna": "kilogramy",
         "Jablka": "kilogramy",
         "Piwo": "sztuki",
         "Papierosy z kiosku": "sztuki",
         "Gumy do zucia": "opakowania"}

#print(skroty.values())
#wartosci = [if "sztuki" in skroty.values()]
#wartosci = {key: value == "sztuki" for key, value in skroty.items()}
#print(wartosci)


#for klucz in skroty.keys():
 #   if(skroty.values() == "sztuki":
    #    print(klucz)

#for produkt, wartosc in skroty.items():
 #   if wartosc == "sztuki":
  #      print(produkt)
wartosci = [k for k,wartosc in skroty.items() if wartosc == "sztuki"]
print(wartosci)