"""Control o gestión de excepciones"""

"""
Crear una app usando excepciones donde no se pueda realizar
la suma entre diferentes tipos de datos
"""


def operations(a, b):
    try:
        result = a + b
    except TypeError:
        print(f"Cannot sum value of type {type(a)} with value of type {type(b)}")
    except ZeroDivisionError:
        print(f"Cannot divide {a} by zero")
    else:
        # 'else' only executes if no exception is raised in the try block
        print(f"Result: {result}")


operations("a", "b")
operations(1, 2)
operations(1, "2")
