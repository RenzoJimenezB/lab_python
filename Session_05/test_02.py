"""Control o gestión de excepciones"""

"""
TypeError
ZeroDivisionError
IndexError
KeyError
FileNotFoundError
ImportError
OverFlowError
"""

"""Estructura y uso"""

"""
try:
    code snippet 1
except 'exception':
    code snippet 2
else:
    code snippet 3
"""


def division(a, b):
    try:
        result = a / b
    except ZeroDivisionError:
        print(f"It is not possible to divide {a} by {b}")
        result = 0
        print(f"Result: {result}")
    else:
        print(f"Result: {result}")


division(1000, 2)
division(400, 0)
