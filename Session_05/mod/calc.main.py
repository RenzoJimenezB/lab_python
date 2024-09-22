from functions import addition as operation_1, multiplication as operation_2

var1 = int(input("Enter first number: "))
var2 = int(input("Enter second number: "))

result_addition = operation_1(var1, var2)
print(result_addition)

result_multiplication = operation_2(var1, var2)
print(result_multiplication)
