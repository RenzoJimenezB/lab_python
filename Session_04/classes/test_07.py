# Polymorphism
# Allows objects of different classes to be treated uniformly
# based on shared method names
# Allows for flexibility and dynamic behaviour

class Dog:
    # static method: do not depend on the instance of the class
    def sonido(self):  # Do not use or modify instance variables
        print("Wuff")


class Cow:
    @staticmethod
    def sonido():  # Since static methods don't operate on instance data
        # they don't need the self parameter
        print("Moo")


class Cat:
    @staticmethod
    def sonido():
        print("Miau")


a_dog = Dog()
a_cow = Cow()
a_cat = Cat()

animals_list = [a_dog, a_cow, a_cat]


def sing(animals):
    for animal in animals:
        animal.sonido()
        # Polymorphism allows you to call the same method on different objects
        # Python automatically figures out which version of the method to execute
        # based on the object's class


sing(animals_list)
