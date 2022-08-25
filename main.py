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

        j = 0
        guesslist = []
        numberstoguess = len(secretNum)
        while j < numberstoguess:
            guess = input(f"guess number {j+1}: ")

            try:
                if lownum <= int(guess) <= highnum:
                    guesslist.append(int(guess))
                    j += 1

                else:
                    print(f"please enter a character between {lownum} and {highnum}")
            except ValueError:
                print("please enter a valid number")


        '''guess1 = input("Guess first number: ")
        guess2 = input("Guess second number: ")
        guess3 = input("Guess third number: ")
        guess4 = input("Guess fourth number: ")

        guesslist = [guess1, guess2, guess3, guess4]'''

        guessNum += 1

        # check if the values are present

        for num in guesslist:
            if int(num) in tempSecret:
                rightNum.append(num)
                tempSecret.remove(int(num))

        # check the values of are in the correct position
        i = 0
        while i < 4:
            if int(guesslist[i]) == secretNum[i]:
                rightPos.append(guesslist[i])
                i += 1
            else:
                i += 1

        print(f"your guess: {guesslist}")
        print(f"you have guessed {len(rightNum)} correct numbers")
        print(f"you have guessed {len(rightPos)} numbers in the correct position")
        if len(rightPos) == 4:
            print(f"You got it! the number was {secretNum}")
            break

    if len(rightPos) != 4:
        print(f"you didn't get the number, the number was {secretNum}")


mastermind(10, 0, 9)
