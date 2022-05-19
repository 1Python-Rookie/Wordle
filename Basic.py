# 1. Hello World
print("Hello World")
# 2. Shape
print("    /|")
print("   / |")
print("  /  |")
print(" /   |")
print("/____|")
print("This is a triangle. WOW!")
# 3. Variables
# Original
print("I am learning how to write python code")
print("aehfgwaekf python")
print("python yeet")
# With variable-Make value of the variable whatever you want and it will substitute it in all the variables throughout
# the code
change_name = "Java"
print("I am learning how to write " + change_name + " code")
print("aehfgwaekf " + change_name)
print(change_name + " yeet")
change_name = "pyhton"
print("skjsfsfh " + change_name + " sjfnskghs")
yasir = "4"
print("This is going to take " + yasir + " years")
# 4. Strings
print("Adam is so good at coding\nhe is learning off of youtube")
# \n means switch lines
print("I am going to use quotes now \"boom\" and also backlashes/")
# \" means quotes / means slash
# Functions using variables
Adam = "Basketball and Golf"
print(Adam.center(200) )
print(Adam.upper() + " baby")
# .is are true/false statements
print(Adam.islower())
print(Adam.lower().islower())
print(len(Adam))
print(Adam[3])
print(Adam.index("k"))
print(Adam.replace("Golf", "fishing"))
print(Adam.replace("o","a"))
# 5. Numbers
print(-2+8)
# gives remainder of 30/7
print(30 % 7)
adam = 3
print(adam)
print(str(adam) + " years")
# If variable doesn't have quotes need to make number a string to add other stuff to the print
yes = -3
print(abs(yes))
print(pow(3,2))
print(min(2342,923203))
print(round(7.23))
from math import *
print(floor(3.4))
print(ceil(3.1))
print(sqrt(16))
# 6. Inputs
age = input("How old are you?")
name = input("What is your name?")
print("This requires an old person at least " + age + " years old. Nice name by the way, " + name)

