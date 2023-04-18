from art import logo

print(logo)


def add(a, b):
    return a+b


def sub(a, b):
    return a-b


def mul(a, b):
    return a*b


def div(a, b):
    return a/b


operations = ["+", "-", "*", "/"]


operation_dict = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div,
}


def calculator():
    try_again = True
    num1 = float(input("What's is your first numner?"))
    for operation in operation_dict:
        print(operation)
    current_answer = num1

    while (try_again):
        valid = False
        while (not valid):
            operation_symbol = input(
                "Which operation do you want to perform from the above")
            if (operation_symbol in operations):
                valid = True

        num2 = float(input("What's is your second numner?"))

        current_answer = operation_dict[operation_symbol](current_answer, num2)
        print(
            f"{current_answer} {operation_symbol} {num2} = {current_answer}")

        try_again_input = input(
            f"Type 'y' to continue with {current_answer} or type 'n' to try with new numbers or e to exit")

        if (try_again_input == "y"):
            try_again = True
        elif (try_again_input == "n"):
            try_again = False
            calculator()
        else:
            try_again = False
            print(f"Your final result is {current_answer}")


calculator()
