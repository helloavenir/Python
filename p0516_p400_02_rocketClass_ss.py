class Rocket:
    def __init__(self):
        self.x = 0
        self.y = 0

    def __str__(self):
        msg = '로켓의 x 좌표: ' + str(self.x) + ' 로켓의 y 좌표: ' + str(self.y)
        return msg

    def moveUp(self):
        self.y += 1


myRocket = Rocket()
print(myRocket)
print('로켓의 높이: ', myRocket.y)

print()

myRocket.moveUp()
print(myRocket)
print('로켓의 높이: ', myRocket.y)
