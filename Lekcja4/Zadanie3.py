with open("Lekcja4/Do_zadania1.py","a") as plik:
    plik.write("\nSiema, to ja pietrek wracam do swiata zywych")
    plik.close()

with open("Lekcja4/Do_zadania1.py","r") as plik:
    for linia in plik:
        print(linia, end="")
    plik.close()