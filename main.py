"""
Python calculator
"""

def addition(num1, num2) -> float:
    return num1 + num2

def subtraction(num1, num2) -> float:
    return num1 - num2

def multiplication(num1, num2) -> float:
    return num1 * num2

def division(num1, num2) -> float:
    if num2 == 0:
        raise ValueError("The second number cannot be zero.")
    return num1 / num2

def main():
    print("Welcome to the Python calculator!")
    print("Select operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    while True:
        choice = input("Enter choice (1/2/3/4): ")

        if choice in ('1', '2', '3', '4'):
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print(f"{num1} + {num2} = {addition(num1, num2)}")
            elif choice == '2':
                print(f"{num1} - {num2} = {subtraction(num1, num2)}")
            elif choice == '3':
                print(f"{num1} * {num2} = {multiplication(num1, num2)}")
            elif choice == '4':
                try:
                    print(f"{num1} / {num2} = {division(num1, num2)}")
                except ValueError as e:
                    print(e)
        else:
            print("Invalid Input")
            
        continue_choice = input("Would you like to continue? (yes/no): ").strip().lower()
        if continue_choice not in ['yes', 'y', 'yea', 'yeah']:
            break
            


if __name__ == "__main__":
    main()