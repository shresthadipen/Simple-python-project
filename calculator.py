def add (a,b):
    return a + b

def subtract(a,b):
    return a - b

def multiply(a,b):
    return a * b

def divide (a,b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error! Division by zero."

def modulus (a,b):
    return a % b

while True:
    print ("Simple calculator")
    print("1. Add\n2. Subtract\n3. Multiply\n4. Divide\n5. Modulus\n6. Exit")
    choice = input("Choose an option: ")

    if choice == '6':
        print("Exit")
        break

    if choice in ['1', '2', '3', '4', '5']:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
            if choice == '1':
                print(f"Sum: {add(num1, num2)}")
            elif choice == '2':
                print(f"Difference: {subtract(num1, num2)}")
            elif choice == '3':
                print(f"Product: {multiply(num1, num2)}")
            elif choice == '4':
                print(f"Division: {divide(num1, num2)}")
            elif choice == '5':
                print(f"Modulus: {modulus(num1, num2)}")
    else:
        print("Invalid choice. Try again.")