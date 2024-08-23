def add(x, y):
    return x + y

def subtract(x, y):
    return x - y

def multiply(x, y):
    return x * y

def divide(x, y):
    if y != 0:
        return x / y
    else:
        return "Error! Division by zero."

def calculator():
    print("Welcome to the Basic Arithmetic Calculator!")
    while True:
        print("\nChoose an operation:\n1.Add\n2.Subtract\n3.Multiply\n4.Divide\n5.Exit")
        
        try:
            option = int(input("Enter your choice (1/2/3/4/5): "))
            if option == 5:
                print("Goodbye! Have a great day.")
                break
            if option in [1, 2, 3, 4]:
                number1 = float(input("Please enter the first number: "))
                number2 = float(input("Please enter the second number: "))
                if option == 1:
                    result = add(number1, number2)
                    print(f"Addition Result: {result}")
                elif option == 2:
                    result = subtract(number1, number2)
                    print(f"Subtraction Result: {result}")
                elif option == 3:
                    result = multiply(number1, number2)
                    print(f"Multiplication Result: {result}")
                elif option == 4:
                    result = divide(number1, number2)
                    print(f"Division Result: {result}")
            else:
                print("Invalid selection! Please choose a number between 1 and 5.")
        except ValueError:
            print("Invalid input! Please enter a valid number.")

calculator()