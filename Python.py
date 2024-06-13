import math

def display_menu():
    print("Scientific Calculator")
    print("=====================")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Power (^)")
    print("6. Square Root (sqrt)")
    print("7. Sine (sin)")
    print("8. Cosine (cos)")
    print("9. Tangent (tan)")
    print("10. Logarithm (log)")
    print("11. Exit")
    print("Choose an operation: ", end='')

def main():
    while True:
        display_menu()
        choice = int(input())

        if choice == 11:
            print("Exiting the calculator. Goodbye!")
            break

        if choice < 1 or choice > 11:
            print("Invalid choice. Please try again.")
            continue

        if choice >= 1 and choice <= 4:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        else:
            num1 = float(input("Enter the number: "))

        if choice == 1:
            result = num1 + num2
            print(f"Result: {num1} + {num2} = {result}")
        elif choice == 2:
            result = num1 - num2
            print(f"Result: {num1} - {num2} = {result}")
        elif choice == 3:
            result = num1 * num2
            print(f"Result: {num1} * {num2} = {result}")
        elif choice == 4:
            if num2 == 0:
                print("Error: Division by zero is not allowed.")
            else:
                result = num1 / num2
                print(f"Result: {num1} / {num2} = {result}")
        elif choice == 5:
            num2 = float(input("Enter the power: "))
            result = math.pow(num1, num2)
            print(f"Result: {num1} ^ {num2} = {result}")
        elif choice == 6:
            if num1 < 0:
                print("Error: Square root of a negative number is not allowed.")
            else:
                result = math.sqrt(num1)
                print(f"Result: sqrt({num1}) = {result}")
        elif choice == 7:
            result = math.sin(num1)
            print(f"Result: sin({num1}) = {result}")
        elif choice == 8:
            result = math.cos(num1)
            print(f"Result: cos({num1}) = {result}")
        elif choice == 9:
            result = math.tan(num1)
            print(f"Result: tan({num1}) = {result}")
        elif choice == 10:
            if num1 <= 0:
                print("Error: Logarithm of a non-positive number is not allowed.")
            else:
                result = math.log(num1)
                print(f"Result: log({num1}) = {result}")
        else:
            print("Invalid operation.")

if __name__ == "__main__":
    main()

