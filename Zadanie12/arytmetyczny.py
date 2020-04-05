def suma(a1, r, ile):
    poczatek = a1
    suma = 0
    i = 0
    while i < ile:
        suma = suma + a1
        a1 = a1 + r
        i=i+1
    print("Suma ciagu arytmetycznego o początowej a1=",poczatek,"r=",r,",oraz o długości=",ile," \nwynosi:",suma)

def różnica(a1, a2):
    if a1 < a2:
        r = a2 - a1
    elif a1 > a2:
        r = a1 - a2
    else:
        r =0
    print("Różnica tego ciągu arytmetycznego wynosi:",r)

def n_wyraz_aryt(a1, r, ile):
    n = a1 + (ile - 1)*r
    print(ile,"wyraz tego ciągu wynosi:",n)

