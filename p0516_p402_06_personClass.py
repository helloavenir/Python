class Person:
    def __init__(self, name, mobile=None, office=None, email=None):
        self.name = name
        self.mobile = mobile
        self.office = office
        self.email = email

    def __str__(self):
        msg = 'name : ' + self.name
        msg += '\nmobile : ' + str(self.mobile)
        msg += '\noffice : ' + str(self.office)
        msg += '\nemail : ' + str(self.email)
        return msg

    def getName(self, name):
        return self.name

    def setName(self, name):
        self.name = name
    


p1 = Person('Kim', 4567, 7799, 'aa@naver.com')
p2 = Person('Kim', office = 7890)
print(p1)
print(p2)


        

     
        
