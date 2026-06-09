def addition(a, b):
    return a + b


def floor_division(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a // b

def subtraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

def power(a, b):
    return a ** b


def modulus(a, b):
    return a % b


a = float(input("Enter first number: "))
b = float(input("Enter second number: "))

print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Power")
print("6. Modulus")
print("7. Floor Division")

choice = int(input("Enter choice: "))

if choice == 1:
    print("Result =", addition(a, b))
elif choice == 2:
    print("Result =", subtraction(a, b))
elif choice == 3:
    print("Result =", multiplication(a, b))
elif choice == 4:
    print("Result =", division(a, b))
elif choice == 5:
    print("Result =", power(a, b))
elif choice == 6:
    print("Result =", modulus(a, b))
elif choice == 7:
    print("Result =", floor_division(a, b))
else:
    print("Invalid Choice")