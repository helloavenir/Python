class Person:
    def __init__(self, name, mobile=None, office=None, email=None):
        self.name = name
        self.mobile = mobile
        self.office = office
        self.email = email

    def setMobile(self, number):
        self.mobile = number

    def setOffice(self, number):
        self.office = number

    def setEmail(self, em):
        self.email = em

    def __str__(self):
        msg = ''
        msg += self.name + '\n'
        msg += 'mobile phone: ' + str(self.mobile) + '\n'
        msg += 'office phone: ' + str(self.office) + '\n'
        msg += 'email address: ' + str(self.email) + '\n'
        return msg
        
       

class PhoneBook():
    def __init__(self):
        self.contacts = {}

    def add(self, name, mobile=None, office=None, email=None):
        p = Person(name, mobile, office, email)
        self.contacts[name] = p      #name을 키로 하는 딕셔너리

    def __str__(self):
        msg = ''
        for p in self.contacts:
            msg += str(self.contacts[p]) + '\n'
        return msg

obj = PhoneBook()

print(obj)


obj.add('Lee',office='1234')
obj.add('Jang', '01077977797', '023456789','kind@naver.com')
print(obj)
        
