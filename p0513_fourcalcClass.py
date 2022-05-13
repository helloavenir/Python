class Calculator :
    def __init__(self,num1=0,num2=0) :
        self.num1 = num1
        self.num2 = num2        
        
    def setdata(self, num1, num2) :
        self.num1 = num1
        self.num2 = num2
        
    def add(self) :
        return self.num1 + self.num2

    def sub(self) :
        return self.num1 - self.num2

    def multi(self) :
        return self.num1 * self.num2

    def div(self) :
        return self.num1 / self.num2


calc1 = Calculator()
calc1.setdata(23,33)
print(calc1.add())


    
        
