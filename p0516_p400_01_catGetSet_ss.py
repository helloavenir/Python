class Cat:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        msg = self.name + ' ' + str(self.age)

    def getName(self):
        return self.name
    
    def getAge(self):
        return self.age
    
    def setName(self, name):
        self.name = name

    def setAge(self, age):
        self.age = age


missy = Cat('Missy', 3)
lucky = Cat('Lucky', 5)

print(missy)
print(lucky)
        

    

    

    

    
    
