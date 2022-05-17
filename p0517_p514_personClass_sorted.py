# Person 클래스에 이름과 나이 저장하고, 나이순으로 정렬하여 보여주는 프로그램


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return '<이름: %s, 나이: %s>' %(self.name, self.age)

def keyAge(person):
    return person.age

people = [Person('홍길동',20), Person('최자영',35), Person('표진인',12)]

print(sorted(people, key = keyAge))
