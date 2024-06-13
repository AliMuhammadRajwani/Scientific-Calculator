Python Scientific Calculator

### Full Description of the Python Scientific Calculator Code

#### 1. **Importing Libraries**
```python
import math
```
- **math Library**: The `math` library is imported to provide access to various mathematical functions such as `pow`, `sqrt`, `sin`, `cos`, `tan`, and `log`.

#### 2. **Display Menu Function**
```python
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
```
- **Function Purpose**: This function displays the list of available operations to the user, including arithmetic operations (addition, subtraction, multiplication, and division) and scientific operations (power, square root, sine, cosine, tangent, and logarithm).
- **Menu Options**: It shows a menu with numbers (1 to 11), each corresponding to an arithmetic or scientific operation or the exit option.

#### 3. **Main Function**
```python
def main():
    while True:
        display_menu()
        choice = int(input())
```
- **Infinite Loop**: The program uses a `while True` loop to repeatedly display the menu and process user inputs until the user decides to exit.
- **Menu Display and User Input**: The `display_menu` function is called to show the menu, and the user's choice is read using `input()`, which is then converted to an integer.

#### 4. **Exit Condition**
```python
        if choice == 11:
            print("Exiting the calculator. Goodbye!")
            break
```
- **User Selection to Exit**: If the user selects option 11, a goodbye message is displayed, and the loop is terminated using `break`, which ends the program.

#### 5. **Input Validation**
```python
        if choice < 1 or choice > 11:
            print("Invalid choice. Please try again.")
            continue
```
- **Validating User Choice**: The program checks if the user's choice is between 1 and 11. If the choice is invalid, an error message is displayed, and the loop continues to prompt the user again.

#### 6. **Reading Operands**
```python
        if choice >= 1 and choice <= 4:
            num1 = float(input("Enter the first number: "))
            num2 = float(input("Enter the second number: "))
        else:
            num1 = float(input("Enter the number: "))
```
- **User Prompts**: For the first four operations (addition, subtraction, multiplication, and division), the user is prompted to enter two numbers. For the other operations, only one number is needed.

#### 7. **Performing Operations**
```python
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
```
- **Arithmetic Operations**: Based on the user's choice, an `if-elif` statement is used to perform the corresponding arithmetic operation:
  - **Addition**: Adds `num1` and `num2` and prints the result.
  - **Subtraction**: Subtracts `num2` from `num1` and prints the result.
  - **Multiplication**: Multiplies `num1` and `num2` and prints the result.
  - **Division**: Divides `num1` by `num2` and prints the result, with a check to prevent division by zero.

```python
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
```
- **Scientific Operations**: Similarly, `if-elif` statements are used to perform scientific operations:
  - **Power**: Raises `num1` to the power of `num2` and prints the result.
  - **Square Root**: Calculates the square root of `num1` and prints the result, with a check to prevent calculation on negative numbers.
  - **Sine**: Calculates the sine of `num1` and prints the result.
  - **Cosine**: Calculates the cosine of `num1` and prints the result.
  - **Tangent**: Calculates the tangent of `num1` and prints the result.
  - **Logarithm**: Calculates the natural logarithm of `num1` and prints the result, with a check to prevent calculation on non-positive numbers.

#### 8. **Program Termination**
```python
if __name__ == "__main__":
    main()
```
- **Main Function Call**: This line ensures that the `main()` function is called when the script is run, starting the program's execution.

### Summary

The Python scientific calculator program is designed to perform both basic arithmetic operations and advanced scientific calculations. It includes a menu-driven interface that continuously prompts the user for input, validates the choices, performs the selected operations, and displays the results. The program handles errors such as invalid menu choices and invalid mathematical operations (like division by zero and taking the logarithm of a non-positive number). The loop runs until the user chooses to exit, ensuring an interactive and user-friendly experience.
