def Upper(wyraz):
    for index in range(len(wyraz)):
        yield wyraz[index].upper()

generator = Upper("siemaneczko")
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print("Eluwina")
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))