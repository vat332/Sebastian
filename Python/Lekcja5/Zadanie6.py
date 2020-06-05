class Wspak:
    """Iterator zwracający wartości w odwróconym porządku"""
    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]

cos = Wspak("Polska")


print(next(cos))
print(next(cos))
print(next(cos))
print(next(cos))
print(next(cos))
print(next(cos))