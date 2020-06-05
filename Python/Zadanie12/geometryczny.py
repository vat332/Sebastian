def suma(a1, q, ile):
    poczatek = a1
    suma = 0
    i = 0
    while i < ile:
        suma = suma + a1
        a1 = a1 * q
        i=i+1
    print("Suma ciagu geometrycznego o początowej a1=",poczatek,"q=",q,",oraz o długości=",ile," \nwynosi:",suma)

def n_wyraz_geo(a1, q, ile):
    n = a1 * q**(ile-1)
    print(ile,"wyraz ciągu geometyrcznego wynosi:",n)

def różnica_geo(a1, a2):
    if a1 < a2:
        q = a2/a1
        print("Różnica wynosi:",q)
    elif a1 > a2:
        q = a1/a2
        print("Różnica wynosi:",q)
    elif (a1 and a2) == 0:
        print("Nie moze być 0!")

