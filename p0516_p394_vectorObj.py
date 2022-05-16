class Vector2D:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        msg ='x 좌표는' + str(self.x) + ', y 좌표는' + str(self.y)
        return msg

    def __add__(self, other):
        return Vector2D(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        return Vector2D(self.x - other.x, self.y - other.y)
    
    def __eq__(self, other):
        return self.x == other.x, self.y == other.y

    
u = Vector2D(0, 1)
v = Vector2D(1, 0)
w = u + v
z = u - v

print(w)
print(z)


