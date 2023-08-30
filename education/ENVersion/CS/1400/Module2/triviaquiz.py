print ("Avatar: The Last Airbender")
score = 0

question1 = input("For how long was Aang in the iceberg? A.100 B.89 C.112:")
if question1 == "100" or question1 == "A" or question1 == "a" or question1 == "A.100" or question1 == "A." or question1 == "a.":
    score += 1
    print ("Question 1: correct")
else:
    print ("Question 1: incorrect")
question2 = input("Who found aang in the Iceberg?")
if question2 == "Sokka and Katara" or question2 == "Sokka Katara" or question2 == "Sokka, Katara":
    score += 1
    print ("Question 2: correct")
else:
    print ("Question 2: incorrect")
question3 = input("Who started the 100 year war? A.Water Tribe B.Earth Kingdom C.Fire Nation:")
if question3 == "C.Fire Nation" or question3 == "C." or question3 == "c." or question3 == "Fire Nation" or question3 == "C" or question3 == "c":
    score += 1
    print ("Question 3: correct")
else:
    print ("Question 3: incorrect")
question4 = input("What are the four elements? List them accordingly:")
if question4 == "water, earth, fire, air" or question4 == "water earth fire air":
    score += 1
    print ("Question 4: correct")
else:
    print ("Question 4: incorrect")
question5 = input("What is the name of the earthbender, who is blind?")
if question5 == "toph" or question5 == "Toph":
    score += 1
    print ("Question 5: correct")
else:
    print ("Question 5: incorrect")

print ("Total score:", score)

if (score == 4 or score == 5):
    print ("You love Avatar: The Last Airbender!")
elif (score == 3 or score == 2):
    print ("Catch up with Avatar: the Last Airbender!")
elif (score == 1 or score == 0):
    print ("You should start watching Avatar: the Last Airbender!")



