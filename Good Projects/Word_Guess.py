import random

options = ["Pizza", "Tower", "Fire", "Red", "Basketball", "Seven", "Math", "Computer", "Tree", "Happy"]
# Computer randomly choosing a word from the list learned from
# https://pynative.com/python-random-choice/#:~:text=Use%20the%20random.,this%20function%20can%20repeat%20items.
word = random.choice(options)
print(word)

# //test test
def game(predict):
    count = 0
    while count < 6:
        prompt = input("Guess a word: ")
        if prompt.upper() == word.upper():
            print("Correct! It was " + word)
            # Learned from https://www.pythontutorial.net/python-basics/python-break/
            break
        else:
            print("Wrong")
        count = count + 1
    guess = count + 1
    if count < 6:
        if guess == predict:
            print("You got the word right and guessed " + str(guess) + " tries!")
        else:
            print("You got the right word but not the amount of tries")
            print("You did it in " + str(guess) + " tries")
    else:
        print("Better luck next time. It was " + word)


# From https://pythonguides.com/python-ask-for-user-input/
while True:
    try:
        tries = int(input("How many tries do you think it will take? "))
        if tries <= 6:
            print("Alright let's see")
            break
        else:
            print("You only have 6 tries")
    except ValueError:
        print("Please type a number")
        continue
hints = {
    "Pizza": "It is an italian food",
    "Tower:": "It is a word for a building",
    "Fire": "It is really hot",
    "Red": "It is a color",
    "Basketball": "It is a sport",
    "Seven": "It is a number",
    "Math": "It is a subject",
    "Computer": "It's a technological device",
    "Tree": "It is a plant",
    "Happy": "It is a feeling"

}
while True:
    hint = input("Would you like a hint? ")
    if hint.upper() == "NO":
        break
    elif not hint.upper() == "YES":
        print("Type Yes or No")
        continue
    else:
        print(hints[word])
        break
game(tries)
