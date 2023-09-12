#Claculator using python
# displaying the menu for user
def menu_display():
    print("Choose the operation from the following:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Quit")
    option = input("Enter the number of your choice: ")
    return option

#function for different mathematical ooperations
def addition(number1, number2):
    return number1 + number2

def subtraction(number1, number2):
    return number1 - number2

def multiplication(number1, number2):
    return number1 * number2

def division(number1, number2):
    if number2 == 0:
        return "Cannot divide by zero."
    return number1 / number2

while True:
    option = menu_display()

    if option == "5":
        print("Exiting the calculator.")
        break

    if option in ("1", "2", "3", "4"):
        number1 = float(input("Enter the first number: "))
        number2 = float(input("Enter the second number: "))

        if option == "1":
            result = addition(number1, number2)
        elif option == "2":
            result = subtraction(number1, number2)
        elif option == "3":
            result = multiplication(number1, number2)
        elif option == "4":
            result = division(number1, number2)

        print("Result:", result)

    else:
        print("Invalid choice. Please select a valid option.")
