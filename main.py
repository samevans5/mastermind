import random


def mastermind(guesses, lownum, highnum):
    # generate 4 digit number into a list
    randNum1 = random.randint(lownum, highnum)
    randNum2 = random.randint(lownum, highnum)
    randNum3 = random.randint(lownum, highnum)
    randNum4 = random.randint(lownum, highnum)
    secretNum = [randNum1, randNum2, randNum3, randNum4]

    # prompt user to input a guess
    guessNum = 1
    while guessNum <= int(guesses):  # limits guesses to guesses input
        rightNum = []
        rightPos = []
        tempSecret = []
        for num in secretNum:
            tempSecret.append(num)
        print(f"Guess number {guessNum}")
        guess1 = input("Guess first number: ")
        guess2 = input("Guess second number: ")
        guess3 = input("Guess third number: ")
        guess4 = input("Guess fourth number: ")

        guess = [guess1, guess2, guess3, guess4]
        guessNum += 1

    # check if the values are present

        for num in guess:
            if int(num) in tempSecret:
                rightNum.append(num)
                tempSecret.remove(int(num))

    # check the values of are in the correct position
        i = 0
        while i < 4:
            if int(guess[i]) == secretNum[i]:
                rightPos.append(guess[i])
                i += 1
            else:
                i += 1

        print(f"you have guessed {len(rightNum)} correct numbers")
        print(f"you have guessed {len(rightPos)} numbers in the correct position")
        if len(rightPos) == 4:
            print(f"You got it! the number was {secretNum}")
            break

    if len(rightPos) != 4:
        print(f"you didn't get the number, the number was {secretNum}")


mastermind(10, 0, 9)
