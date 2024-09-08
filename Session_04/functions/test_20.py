num_1 = int(input("Ingrese un número: "))
num_2 = int(input("Ingrese un número: "))
num_3 = int(input("Ingrese un número: "))
num_4 = int(input("Ingrese un número: "))


def find_greatest(a, b, c, d):
    if a > b and a > c and a > d:
        return a
    elif b > a and b > c and b > d:
        return b
    elif c > a and c > b and c > d:
        return c
    else:
        return d


def find_maximum(a, b, c, d):
    return max(a, b, c, d)


def get_largest_number(a, b, c, d):
    greatest = a
    if b > a:
        greatest = b
    if c > a:
        greatest = c
    if d > a:
        greatest = d
    return greatest


def max_of_numbers(a, b, c, d):
    list_numbers = []
    list_numbers.extend([a, b, c, d])
    list_numbers.sort()
    return list_numbers[-1]


result = pow(max_of_numbers(num_1, num_2, num_3, num_4), 3)
print(result)
