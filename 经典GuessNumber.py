import numpy as np

print("let's guess a number between 1 and 100!")

number = np.random.randint(0,101)

while True:
    try:
        guess = int(input("Now,guess it: "))
    except ValueError:
        print("hey my honey, We guess number not you mind!")
        continue
    if guess > number:
        print("OH MY GOD! It's so big!")
    elif guess < number:
        print(("what a pitty! It's so small!"))
    else:
        print("FUck! you made it!")
        print("Time to say good bye!")
        break
