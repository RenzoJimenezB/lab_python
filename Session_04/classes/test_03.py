class Car:
    wheels = 4

    def __init__(self, colour, acceleration):
        self.colour = colour
        self.acceleration = acceleration
        self.speed = 0

    def accelerate(self):
        self.speed += self.acceleration

    def brake(self):
        self.speed -= self.acceleration
        if self.speed < 0:
            self.speed = 0


car_1 = Car("Yellow", 20)
print(f"The speed of the car is {car_1.speed}mph")

car_1.accelerate()
car_1.accelerate()
car_1.accelerate()
car_1.accelerate()
print(f"The new speed of the car is {car_1.speed}mph")

car_1.brake()
car_1.brake()
print(f"The speed of the car now is {car_1.speed}mph")
