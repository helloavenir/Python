class Counter :
    def __init__(self, initValue = 0) :
        self.count = initValue
    def increment(self) :
        self.count += 1

a = Counter(100)
print('count의 값 : ', a.count)
a.increment()
print('count의 값 : ', a.count)

b=Counter()
print('count의 값 : ', b.count)
b.increment()
print('count의 값 : ', b.count)
