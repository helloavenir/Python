class Counter :
    def __init__(self) :
        self.count = 0

    def increment(self) :
        self.count += 1



a=Counter()
print(a.count)
a.increment()
print(a.count)
a.increment()
a.increment()
print(a.count)
