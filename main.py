def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations_dict = {
                    "+": "add",
                    "-": "subtract",
                    "*": "multiply",
                    "/": "divide"}

first_number = float(input("What is the first number? "))
continue_calculation = True

while continue_calculation:
    for i in operations_dict:
        print(i)
    operation_symbol = input("Pick an operation: ")
    calculation_function = operations_dict[operation_symbol]

    next_number = float(input("What is the next number? "))

    #calling a function by its name when the function's name is stored in a string using 'globals()' dictionary
    if calculation_function in globals():
        result = globals()[calculation_function](first_number, next_number)
        print(f"{first_number} {operation_symbol} {next_number} = {result}")

        more_calculation = input(f"Do you want to continue calculating with '{result}'? Type Y/N: ").upper()
        if more_calculation == "Y":
            first_number = result
        elif more_calculation == "N":
            continue_calculation = False