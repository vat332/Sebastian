def fibb(n):
    a, b = 0, 1
    for n in range(n):
        a, b = b, a + b
        yield (a)

#for fibo in fibb(11):
 #   print(fibo)
#print(next(fibb(9)))
fibbonaci = fibb(11)
print(next(fibbonaci))
print(next(fibbonaci))
print(next(fibbonaci))
print(next(fibbonaci))
print(next(fibbonaci))
print(next(fibbonaci))
print(next(fibbonaci))
print(next(fibbonaci))
print(next(fibbonaci))
print(next(fibbonaci))
print(next(fibbonaci))
print(next(fibbonaci))


#print(fibbonaci.__next__())
#print(fibbonaci.__next__())
#print(fibbonaci.__next__())
#print(fibbonaci.__next__())
#print(fibbonaci.__next__())
#print(fibbonaci.__next__())
#print(fibbonaci.__next__())
#print(fibbonaci.__next__())
#print(fibbonaci.__next__())
#print(fibbonaci.__next__())
#print(fibbonaci.__next__())
#print(fibbonaci.__next__())



