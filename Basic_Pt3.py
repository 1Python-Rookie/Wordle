print("Hi")
# 15. Dictionary
month = {
    "Jan": "January",
    "Feb": "Feburary",
    "Mar": "March",
}

print(month["Mar"])
print(month.get("Feb"))
print(month.get("yeet", "Error"))

# 16. While Loops
h = 2
while h < 5:
    # Add condition
    print("math")
    print(h)
    h = h + 1
print("end of loop")
# 17. Guessing Game different file
# 18. For Loop
for letter in "Adam":
    print(letter)

people = ["Adam", "Nooh", "Musa", "Harris"]
for person in people:
    print(person)
for index in range(10):
    print(index)
bros = ["Adam", "Nooh", "Musa", "Harris"]
for index in range(len(bros)):
    print(bros[index])

for index in range(5):
    if index == 0:
        print("Uno")
    else:
        print("ok")


# 19. Exponent Function
def power(base, tiny):
    answer = 1
    for INDEX in range(tiny):
        answer = answer * base
    return answer


print(power(3, 3))
# 20. 2D Lists and Nested Loops
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [0]
]
print(grid[0][1])
for row in grid:
    for colomn in row:
        print(colomn)


# 21. Translator
def translate(phrase):
    output = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            output = output + "g"
        else:
            output = output + letter
    return output


print(translate(input("Give a phrase")))
