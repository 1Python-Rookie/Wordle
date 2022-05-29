import random
import time
from Wordle_Lists import words
from Wordle_Lists import first_row
from Wordle_Lists import second_row
from Wordle_Lists import third_row
pick = random.choice(words)
target = list(pick.upper())
for index in range(1, 7):
    print(first_row)
    print(second_row)
    print(third_row)
    while True:
        guess = input("Guess a word ")
        compare = list(guess.upper())
        if len(compare) != 5:
            print("Enter a 5 letter word")
        else:
            print(guess.upper())
            break
    time.sleep(2)
    if compare == target:
        print("Nice job!")
        var: bool = True
        break
    else:
        var: bool = False
        for letter in compare:
            if letter in target:
                if letter == target.index(letter):
                    print(letter + " is in the right spot")
                    target.pop(target[letter])
                else:
                    print(letter + " is in the word but a different spot")
            else:
                print(letter + " is not in the word")
                if letter in first_row:
                    try:
                        first_row.remove(letter)
                    except ValueError:
                        pass
                elif letter in second_row:
                    try:
                        second_row.remove(letter)
                    except ValueError:
                        pass
                else:
                    try:
                        third_row.remove(letter)
                    except ValueError:
                        pass
if not var:
    print("The correct word is " + pick.capitalize())


