import numpy as np

count = 0
fastCount = 10
number = np.random.randint(0,101)

print("let's guess a number between 1 and 100! You noly have 10 chances")

while True:
    if count >= 10:
        print("Oh no! You've used all your chances!"+"The number was: " + str(number))
        print("But we can do it again!(yes/no)")
        if input().lower() == "yes":
            count = 0
            number = np.random.randint(0,101)
            continue
        break

    try:
        guess = int(input("Now,guess it: "))
    except ValueError:
        print("hey my honey, We guess number not you mind!")
        continue

    if guess > number:
        print("OH MY GOD! It's so big!")
        count += 1
    elif guess < number:
        print(("what a pitty! It's so small!"))
        count += 1
    else:
        if count < fastCount:
            fastCount = count
        print("FUck! you made it! just '" + str(count) + "' times")
        print("Your fastest time is '" + str(fastCount) + "' times")
        print("Time to say good bye!")
        print("But do you want to play agein?(yes/no)")
        if input().lower() == "yes":
            count = 0
            number = np.random.randint(0,101)
            continue
        break
print("Bye~")



#最高十次猜数字次数✓   重开✓    记录最快✓ 