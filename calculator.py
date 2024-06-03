# function to return enter input
def check_user_input_enter_key():
    return input("press Enter to continue...\n")


# function to return empty input for numbers
def check_user_input_number():
    return input("")


# function to handle invalid number inputs
def incorrect_number_input():
    print("You have entered an incorrect value, please try again...")
    return input("")


# function to take in user inputs, then display the equation with solution
def print_equation(first_num, second_num, operation):
    first_num = int(first_num)
    second_num = int(second_num)
    if operation == "adding":
        solution: int = first_num + second_num
        print(first_num, "+", second_num, "=", str(solution))
    elif operation == "subtracting":
        solution: int = first_num - second_num
        print(first_num, "-", second_num, "=", str(solution))
    elif operation == "multiplying":
        solution: int = first_num * second_num
        print(first_num, "*", second_num, "=", str(solution))
    elif operation == "dividing":
        solution: int = round((first_num / second_num))
        print(first_num, "/", second_num, "=", str(solution))


# function that handles the end of the program (restart or quit)
def calculator_reset():
    user_input = input("\nWould you like to calculate another solution? (Y/N)")
    user_input = user_input.lower()
    if user_input == "y" or user_input == "yes":
        calculator()
    elif user_input == "n" or user_input == "no":
        quit()
    else:
        print("Invalid Input, try again...")
        calculator_reset()

# main calculator functionality
def calculator():
    print("Welcome to my calculator")
    user_input_enter: str = check_user_input_enter_key()

    while user_input_enter != "":
        user_input_enter = check_user_input_enter_key()
        if user_input_enter == "":
            break

    print("enter your first number")
    user_input_first_number = check_user_input_number()

    print("\nFirst Number: " + user_input_first_number)
    print("\nWhat operation do you want to use in your equation?")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    operation_input = input("")
    operation = ""
    if operation_input == "1":
        operation = "adding"
    elif operation_input == "2":
        operation = "subtracting"
    elif operation_input == "3":
        operation = "multiplying"
    elif operation_input == "4":
        operation = "dividing"
    else:
        incorrect_number_input()

    print("\nFirst Number: " + user_input_first_number)
    print("You are", operation + "...\n")  # adding, subtract, etc...
    print("Enter your second Number")
    user_input_sec_number = check_user_input_number()

    print("\nCalculating....\n")
    print_equation(user_input_first_number, user_input_sec_number, operation)

    calculator_reset()


# start program
calculator()