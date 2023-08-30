#By Villezcas, Elsy
#Program will allow the user to input a sentence it will take the first letter of each word and create an acroynm
#Example: TTYL
#Talk to you later
print ("Acronym Maker")
sentence = ""
while sentence != "q":
    sentence = input("Enter a sentence or q to quit:")
    #pos = position
    pos = 0
    acronym = sentence[0]
    while pos >= 0 and sentence != 0:
        pos = sentence.find (" ", pos)
        if pos >= 0:
            pos += 1
            acronym += sentence [pos]
    if sentence != "q":
        print ("Acronym:", acronym.upper())