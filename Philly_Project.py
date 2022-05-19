import random
from Wordle_Lists import words
from Wordle_Lists import first_row
from Wordle_Lists import second_row
from Wordle_Lists import third_row
pick = random.choice(words)
target = list(pick.upper())
for index in range(1, 7):
    guess = input("Guess a word")
    compare = list(guess.upper())
    print(compare)
    if compare == target:
        print("Nice job")
        win = True
        break
    else:
        win = False
        for letter in range(len(compare)):
            try:
                var = compare[i] == target[target.index(compare[i])] and not compare[i] == target[i]
                working = True
            except ValueError:
                print(compare[i] + " is not in the word")
                working = False
            if working:
                if compare[i] == target[i]:
                    print(compare[i] + " is in the right spot")
                    pass
                else:
                    if compare[i] == target[target.index(compare[i])] and not compare[i] == target[i]:
                        print(compare[i] + " is in the word but a different spot")
            else:
                pass
if not win:
    print("The answer was " + pick.capitalize())