import random

print ("mastermind")
#mastermind is gussing the numbers in the correct position
secret = [1, 2, 3, 4]
#our secrect is what we are supposed to get

#for i in range (4):
    #secret.append(random.randrange(1,5))

#randon.randrange is to set the range that they can pick from

posCorrect = 0
guesses = 0
maxGuesses = 10

#keep the game going till they win or lose

while posCorrect < 4 and guesses < maxGuesses:
    guessArrayString = input("Enter your guess of four numbers:").split()
    guesses += 1
    guessArrayInt = [int(i) for i in guessArrayString]

    tempSecret = secret.copy()
    tempGuessInt = guessArrayInt.copy()
    posCorrect = 0
    for i in range(len(tempSecret)):
        if tempSecret[i] == tempGuessInt [i]:
            posCorrect += 1
            tempSecret[i] = -1
            tempGuessInt[i] = -1
    colorsCorrect = 0
    for i in range(len(tempSecret)):
        for j in range (len(tempGuessInt)):
            if i != j and tempSecret[i] == tempGuessInt[j] and  tempSecret[i] != -1:
                colorsCorrect += 1
                tempSecret[i] = -1
                tempGuessInt[i] = -1
                break 

    print ("Position Correct:", posCorrect)
    print ("Colors Correct:", colorsCorrect)

    if posCorrect == 4:
        print ("You win")
    elif guesses == maxGuesses:
        print ("You lose")

print ("Secret combo was", secret)

    