class Circle :
     def __init__(self, r) :
         self.radius = r

     def area(self) :
         return 3.14*self.radius**2

c1 = Circle(10)
c2 = Circle(5)
c3 = Circle(10)

print(c1.area())
print(c2.area())
print(c3.area())

a = 10
b = 10
if a == b :
    print('equal')

    
if c1 == c3 :
    print('equal')

print()


class Circle :
     def __init__(self, r) :
         self.radius = r

     def area(self) :
         return 3.14*self.radius**2

     def __eq__(self, other) :
         return self.radius == other.radius
        

c1 = Circle(10)
c2 = Circle(5)
c3 = Circle(10)

    
if c1 == c3 :
    print('equal')



    
    
    
