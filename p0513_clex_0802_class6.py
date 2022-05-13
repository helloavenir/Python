class Car :
    def __init__(self, speed, color, model) :
        self.speed = speed
        self.color = color
        self.model = model

    def drive(self) :
        self.speed = 60

    def up_speed(self, speed = 5) :
        self.speed += speed

    def down_speed(self, speed = 5) :
        self.speed -= speed

    def show(self) :
        print(self.speed)

car1 = Car(0, 'red', 'Hybrid')
car2 = Car(0, 'blue', 'Electric')


car1.show()
car1.up_speed()
car1.show()
car1.up_speed(40)
car1.show()
car1.down_speed(15)
car1.show()
car1.drive()
car1.show()

