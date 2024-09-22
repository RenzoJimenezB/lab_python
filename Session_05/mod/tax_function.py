def calculate_tax(salary):
    try:
        if int(salary) > 500:
            total_taxes = salary * 0.8

            print(f"Total taxes: S/{int(total_taxes)}")
            return total_taxes
        else:
            print("You don't have to pay taxes")
            return 0
    except ValueError:
        print(f"Invalid input. Please enter a valid numeric value for salary")
