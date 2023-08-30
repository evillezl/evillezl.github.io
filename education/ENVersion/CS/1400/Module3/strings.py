#steings are a letter
letters = "ABCDEFG"
print (letters)
# The position
# A B C D E F G
# 0 1 2 3 4 5 6
print (letters [1])
# Prints from one point to another 
print (letters [3:6])
#length function
word = input("Enter a word:")
wordLen = len(word)
#len uses to find the length on the input
print (word, "is", wordLen, "letters long")
#Imbed quotes within a string
txt = """She Said, "Knock Knock?"
He replied, "Who's There" """
print (txt)
#string case in upper or lower
word = input ("Enter a word: ")
print ("Upper Case:", word.upper ())
print ("Lower Case:", word.lower ())
#string find, finding the position of the string
txt = "Come and clean the chaos in your closet"
pos = txt.find ("c")
print (pos)

pos = pos + 1
pos = txt.find ("c", pos)
print (pos)

#string replace, replace word with something else 
txt = "Come and clean the chaos in your closet"
print (txt.replace("c", "k"))

    #return the value to the original position
print (txt)
txt = txt.upper ()
print (txt)

#slicing strings 
# : means starting or ending
# :starting at 
# ending at:
txt = "ABCDEFG"
print (txt[:3])
print (txt[3:])

#striping whitespace
txt = " A "
txt = txt.strip ()
print (txt, "END")

#making string together 
txt1 = "ABC"
txt2 = "DEF"
txt3 = txt1 + txt2
print (txt3)
    
#adding with numbers
txt = "GHI"
num = 42
print (txt+num)
