class A:
    def __init__(self):
        self.initial = 10
        self._counter = 0  # single underscore: protected attribute
        # "internal use only" (within the class and its subclasses)
        # Possible to access from outside the class
        # It shouldn't be accessed directly (not part of the public API of the class)

    def increment_counter(self):
        self._counter += 1

    def get_count(self):
        return self._counter


class B:
    def __init__(self):
        self.initial = True
        self.__counter = 0  # name mangling is performed => _ClassName__attribute
        # Private attribute
        # The attribute's name is internally changed to make it less accessible from outside the class
        # Enforces encapsulation
        # Attribute shouldn't be accessed or modified from outside the class

    def increment_counter(self):
        self.__counter += 1

    def get_count(self):
        return self.__counter
        # The method can access to the private attribute within the class
        # Name mangling only affects external access


var_1 = A()
print(f"Get counter A: {var_1.get_count()}")
print(f"Counter A: {var_1._counter}")
print(f"Initial A: {var_1.initial}\n")

var_1.increment_counter()
var_1.increment_counter()
var_1.initial = 20

print(f"Get counter A: {var_1.get_count()}")
print(f"Counter A => {var_1._counter}")
print(f"Initial A => {var_1.initial}\n")

var_2 = B()
print(f"Get counter B: {var_2.get_count()}")
# print(f"Counter B: {var_2.__counter}")
# This will fail because Python has renamed the attribute to "_B__counter"

print(f"Accessing to counter B through its mangled name: {var_2._B__counter}")

print(f"Initial B: {var_2.initial}\n")

var_2.increment_counter()
var_2.increment_counter()
var_2.initial = False

print(f"Get counter B: {var_2.get_count()}")
# print(f"Counter B => {var_2.__counter}")
print(f"Initial B => {var_2.initial}")
