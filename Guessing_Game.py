# 17. Guessing Game
print("Guess a word \n You get 3 tries \n Your only hint is that it is the name of a person")
word = "Najam"
guess = ""
count = 0
limit = 3
empty = False

while guess != word and not empty:
    if count < limit:
        guess = input("Guess a word ")
        count += 1
    else:
        empty = True

if empty:
    print("tuff is was Najam")
else:
    print("noice")