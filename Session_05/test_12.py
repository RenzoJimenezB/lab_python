"""
Decorators
"""


def decoratorFunctionA(functionB):
    def functionC(*args, **kwargs):
        print("1. Before executing function to be decorated ")
        result = functionB(*args, **kwargs)
        print("2. After executing function to be decorated ")
        return result

    return functionC


@decoratorFunctionA
def greet(nombre, apellido, **kwargs):
    print(f"Hello, {nombre} {apellido}!")

    for key, value in kwargs.items():
        print(f"{key}: {value}")


greet("Julio", "Pérez", key1="value1", key2="value2")
