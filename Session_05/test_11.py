"""
Decorators
"""


def decoratorFunctionA(functionB):
    def functionC(*args, **kwargs):
        print("1. Before executing function to be decorated ")
        functionB(*args, **kwargs)
        print("2. After executing function to be decorated ")

    return functionC


@decoratorFunctionA
def greet():
    print("Hello World!")


greet()
