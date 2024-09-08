class Car:
    # class attribute: all instances have the same
    # The property is intended to be the same for all instances
    # Changing a class attribute affects all instances that have not overridden that attribute at the instance level
    wheels = 4

    def __init__(self, colour, acceleration):
        self.colour = colour
        self.acceleration = acceleration
        self.speed = 0
        # An instance attribute may share the same value with other instances
        # Functionally the same, but less semantically clear
        # Instance attributes are used for properties that might vary across instances

    def accelerate(self):
        self.speed += self.acceleration

    def brake(self):
        self.speed -= self.acceleration
        if self.speed < 0:
            self.speed = 0


class FlyingCar(Car):
    wheels = 6  # Overridden class attribute

    def __init__(self, colour, acceleration, flying=False):
        super().__init__(colour, acceleration)  # Initialise the parent class
        # super() calls the parent's constructor and initialises inherited attributes
        # Inherited properties are not required
        """self.colour = colour
        self.acceleration = acceleration"""
        self.flying = flying  # Class own instance attribute

    def fly(self):
        self.flying = True

    def land(self):
        self.flying = False


car_1 = Car("red", 55)
flying_car_1 = FlyingCar("blue", 80)

print(f"My flying car is {flying_car_1.colour}")

print(f"The speed of my flying car is {flying_car_1.speed}mph")
flying_car_1.accelerate()
print(f"The speed of my flying car after accelerating is {flying_car_1.speed}mph")

print(f"My car is flying: {flying_car_1.flying}")
flying_car_1.fly()
print(f"My car is flying: {flying_car_1.flying}")

not_flying_car_wheels = car_1.wheels
print(f"Car has {not_flying_car_wheels} wheels")

flying_car_wheels = flying_car_1.wheels
print(f"Flying car has {flying_car_wheels} wheels")
