# 22. Try/Ecept
try:
    this = 2 / 0
    number = int(input("Give number "))
    print(number)
except ZeroDivisionError as error:
    print(error)
except ValueError:
    print("I said a number")
try:
    h = int(input("Give number "))
    print(h)
except ZeroDivisionError:
    print("Your bad at math")
except ValueError:
    print("I said a number")
# What to do if a user does not listen to prompt
# 23. Reading Files
file = open("Guessing_Game.py", "r")
print(file.readable())
print(file.readline())
print(file.readline())
print(file.readlines()[2])
# .read gives the whole file; .readlines puts every line of the file in a list
# r is read; w is write; a is for adding new info; r+ is reading and writing
file.close()
extra = open("main.py", "a")
extra.write("\n yer")
# Careful not to mess up the file
# w would erase everything and just write what you put in the command
# You can also create files by putting the name of it in the open cammand
extra.close()
