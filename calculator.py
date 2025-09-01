def calculator():
    print("Simple Calculator")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    # Get user input
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        choice = input("Enter your choice (1/2/3/4): ")
    except ValueError:
        print("Invalid input. Please enter a number.")
        return

    # Perform calculation
    if choice == "1":
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif choice == "2":
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif choice == "3":
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    elif choice == "4":
        if num2 != 0:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
        else:
            print("Error: Division by zero is not allowed")
    else:
        print("Invalid choice. Please enter a number between 1 and 4.")

def main():
    calculator()
    while True:
        again = input("Do you want to calculate again? (yes/no): ")
        if again.lower() == "yes":
            calculator()
        elif again.lower() == "no":
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    main()