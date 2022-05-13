class Student:
	def __init__(self, name=None, age=0):
		self.__name = name
		self.__age = age      # __로 정보은닉을 설정한 변수는

	def getAge(self):             # get이 붙은 접근자 메소드를 따로 만들어 접근해줘야 한다.
		return self.__age

	def getName(self):
		return self.__name

	def setAge(self, age):        # set이 붙은 설정자 메소드를 따로 만들어 설정해줘야 한다.
		self.__age=age

	def setName(self, name):
		self.__name=name


obj=Student("Hong", 20)              # 이름을 Hong, 나이를 20으로 입력
print(obj.getName())                 # 정보은닉한 변수 name을 접근자 메소드로 이름에 접근
obj.setName('Kim')                   # 정보은닉한 변수 name을 설정자 메소드로 이름 변경
print(obj.getName())
print()

print(obj.getAge())
obj.setAge(43)
print(obj.getAge())
