import itertools

def kombinacje():
    litery = ['a','b','c','d','e','f','g','h','i','j']
    for i in itertools.combinations(litery,3):
        yield print(i)

x=kombinacje()
while(x != 0):
    next(x)