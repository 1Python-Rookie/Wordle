def to_smash(total_candies, friends=3):
    return print(total_candies % friends)


to_smash(10, 2)


def calculator():
    input_1 = input("Give first number: ")
    symbol = input("Give operation: ")
    input_2 = input("Give second number: ")
    if symbol := "plus":
        return print(input_1 + input_2)
    elif symbol := "-":
        return int(input_1) - int(input_2)
    elif symbol := "times":
        return print(input_1 * input_2)
    elif symbol := "divide":
        return print(input_1 / input_2)
    else:
        print("Error")


calculator()

def test():
    input_1 = input("Give first number: ")
    input_2 = input("Give second number: ")
    return print(input_1 + input_2)




