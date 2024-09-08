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


car_1 = Car("red", 10)
print(f"The colour of my car is: {car_1.colour}")

car_2 = Car("blue", 20)
car_2.miles = 3000
print(f"Miles traveled: {car_2.miles}")
