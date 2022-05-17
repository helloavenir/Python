class Person():
    def __init__(self,name,mobile=None,office=None,email=None):
        self.name = name
        self.mobile = mobile
        self.office = office
        self.email = email

    def setName(self,name):
        self.name = name

    def setMobile(self,number):
        self.mobile = number

    def setOffice(self,number):
        self.office = number

    def setEmail(self,address):
        self.email = address

    def getName(self):
        return self.name
        
    def getMobile(self):
        return self.mobile

    def getOffice(self):
        return self.office

    def getEmail(self):
        return self.email

    def __str__(self):
        msg = 'name : ' + self.name
        msg += '\nmobile : ' + str(self.mobile)
        msg += '\noffice : ' + str(self.office)
        msg += '\nemail : ' + str(self.email)
        return msg

print()
print('-'*50)       
p1 = Person("Kim", office="1234567", email="kim@company.com")
print(p1)
print('-'*50)
p2 = Person("Park", office="2345678")
print(p2)
print('-'*50)
p2.setEmail("park@company.com")
print(p2)
print('-'*50)

