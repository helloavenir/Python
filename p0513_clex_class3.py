class Calculator :
    def __init__(self) :
        self.result = 0
    def add(self, num) :
        self.result += num
        return self.result


calc1=Calculator()
calc2=Calculator()

print(calc1.add(3))
print(calc1.add(4))
print(calc2.add(10))
print(calc2.add(20))
print(calc1.add(5))
print(calc2.add(30))
