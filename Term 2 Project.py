def operations():
    if symbol.upper() == "PLUS" or symbol == "+":
        return print(num_1 + num_2)
    elif symbol.upper() == "MINUS" or symbol == "-":
        return print(num_1 - num_2)
    elif symbol.upper() == "TIMES" or symbol == "*":
        return print(num_1 * num_2)
    elif symbol.upper() == "DIVIDE" or symbol == "/":
        return print(num_1 / num_2)
    else:
        print("You have 4 options: plus, minus, times and divide it's not hard")


input_1 = input("Give first number: ")
num_1 = input_1
try:
    num_1 = float(input_1)
except ValueError:
    print("I said a number. Can't say I didn't warn you")
    num_1 = False
symbol = input("Give operation: ")
input_2 = input("Give second number: ")
num_2 = input_2
try:
    num_2 = float(input_2)
except ValueError:
    print("I said a number")
    num_2 = False


def calculator():
    if num_1 and num_2:
        print("Your input: " + input_1 + " " + symbol + " " + input_2)
        operations()
    else:
        print("You didn't put a number so it won't work genius!")


calculator()
print("THANK YOU FOR YOUR TIME!")