# 7. Lists
listed = ["Pizza", "Donuts", "Ramen", "Rice"]
print(listed[0])
print(listed[2:])
print(listed[1:3])
# 8. List functions
peeps = ["Nooh", "Abdullah", "Musa", "Adam", "Josh"]
numbers = [2, 5, 8, 34, 77, 67, 97]
peeps.extend(numbers)
# Merge lists
print(peeps)
numbers.append("Najam")
# Add string to end of a list
print(numbers)
numbers.insert(3, "Jeff")
# Add string in certain area of list
print(numbers)
numbers.remove(77)
print(numbers)
numbers.clear()
print(numbers)
peeps.pop()
# Pops off a string
print(peeps)
print(peeps.index("Adam"))
# Tells where the string is in the list
this = ["yeet", "yeet", "beat", "feet"]
print(this.count("yeet"))
this.sort()
print(this)
that = this.copy()
print(that)
# 9. Tuples
tuples = (3, 4)
print(tuples[1])


# 10 Functions
def hi():
    print("no")


hi()


def upgrade(details, emotion):
    return "Taking it up a notch" + details + str(emotion)


print(upgrade("this", "that"))


# 11. Return statement
def square(num):
    num * num


square(2)
print(square(2))


def cube(num):
    return num * num * num


# Cannot type anymore code into the function after return


print(cube(2))
answer = cube(3)
print(answer)
# 12. If statements
male = False
dude = True
if male or dude:
    print("Hey dude")
else:
    print("Bye")

me = True
you = False
if me and you:
    print("yes")
else:
    print("no")
# Elif is else if

pizza = True
apple = False
if pizza and apple:
    print("Lets go")
elif pizza and not apple:
    print("Hmmm")
else:
    print("weird")


# 13. If statements and comparisons
def big_num(n1, n2, n3):
    if n1 >= n2 and n1 >= n3:
        return n1
    elif n2 >= n1 and n2 >= n3:
        return n2
    else:
        return n3


print(big_num(7, 42, 6))


def yes(y1, y2):
    if y1 == y2:
        return "equal"
    else:
        return "Nope"


print(yes(4, 4))


def no(b1, b2):
    if b1 != b2:
        return "Nope"
    else:
        return "yes"


(print(no(2, 2)))
# 14. Calculator 2
numero_1 = float(input("Give a number"))
operation = input("Give an operation")
numbero_2 = float(input("Give another number"))

if operation == "+":
    print(numero_1 + numbero_2)
elif operation == "-":
    print(numero_1 - numbero_2)
elif operation == "/":
    print(numero_1 / numbero_2)
elif operation == "*":
    print((numero_1 * numbero_2))
else:
    print("Error")
