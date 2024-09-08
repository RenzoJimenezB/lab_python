class Car:
    wheels = 4

    """Constructor"""

    def __init__(self, colour, acceleration):
        self.colour = colour
        self.acceleration = acceleration
        self.speed = 0

    """Methods"""

    def accelerate(self):
        self.speed += self.acceleration

    def brake(self):
        self.speed -= self.acceleration
        if self.speed < 0:
            self.speed = 0


"""Instantiate a class"""

car_1 = Car("black", 40)
print(f"The colour of my car is: {car_1.colour}")
print(f"My car has {car_1.wheels} wheels")
print(f"The acceleration of my car is: {car_1.acceleration}mph")

car_1.accelerate()
car_1.accelerate()
print(f"The speed of my car is: {car_1.speed}")
