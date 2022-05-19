import random
print("Do you know the Periodic Table of Elements? \nLet's find out!")
symbols = ["H",
           "He",
           "Li",
           "Be",
           "B",
           "C",
           "N",
           "O",
           "F",
           "Ne",
           "Na",
           "Mg",
           "Al",
           "Si",
           "P",
           "S",
           "Cl",
           "Ar",
           "K",
           "Ca",
           "Fe",
           "Ni",
           "Cu",
           "Zn",
           "Se",
           "Br",
           "Kr",
           "Sr",
           "Ag",
           "Sn",
           "I",
           "Xe",
           "Au",
           "Hg",
           "Pb"]
names = {
    "H": "Hydrogen",
    "He": "Helium",
    "Li": "Lithium",
    "Be": "Beryllium",
    "B": "Boron",
    "C": "Carbon",
    "N": "Nitrogen",
    "O": "Oxygen",
    "F": "Fluorine",
    "Ne": "Neon",
    "Na": "Sodium",
    "Mg": "Magnesium",
    "Al": "Aluminum",
    "Si": "Silicone",
    "P": "Phosphorus",
    "S": "Sulfur",
    "Cl": "Chlorine",
    "Ar": "Argon",
    "K": "Potassium",
    "Ca": "Calcium",
    "Fe": "Iron",
    "Ni": "Nickel",
    "Cu": "Copper",
    "Zn": "Zinc",
    "Se": "Selenium",
    "Br": "Bromine",
    "Kr": "Krypton",
    "Sr": "Strontium",
    "Ag": "Silver",
    "Sn": "Tin",
    "I": "Iodine",
    "Xe": "Xeon",
    "Au": "Gold",
    "Hg": "Mercury",
    "Pb": "Lead"
}


def quiz():
    atom = random.choice(symbols)
    answer = names[atom]
    tries = 0
    while tries != 5:
        element_question = input("What is the name of " + atom + "?")
        if not element_question.upper() == answer.upper():
            print("Incorrect, try again ")
            tries = tries + 1
        else:
            print("Correct!")
            break
    if tries == 5:
        print("The answer was " + answer)


while True:
    try:
        i = int(input("How many questions do you want to answer? "))
        if i <= 10:
            print("Confirmed. You will get " + str(i) + " questions")
            break
        else:
            print("You are only allowed 35 questions maximum")
    except ValueError:
        print("Give integer value ")
        continue
for index in range(i):
    quiz()
