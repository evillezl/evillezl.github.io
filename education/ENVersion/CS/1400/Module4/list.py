#list that can include, informaiton, or numbers
#Example:

#mylist
#always have it in square brackets
mylist = ["orange", "tangerine", "manderin"]

#len function to determine the number(length) of items in list
print(len(mylist))

#accessing a single item, starting at 0
print(mylist[1])

#changing a value 
mylist[1]="dragonfruit"
print(mylist)

#appending allows you to add it to the end of the list
mylist.append("tangerine")
print(mylist)

#removing from the list
mylist.remove("orange")
print(mylist)

#mylist 2
#declaring an empty list
#where you start with an empty list and append it
mylist2 = []
mylist2.append("dragonfruit")

#inserting allows you to add in the position you want it to be
mylist2.insert (0,"apricot")
print(mylist2)

#removing the list number
#if you just say pop, with no number, it automatically removes it
mylist2.pop(1)
print(mylist2)

#clearing function
mylist.clear ()
print(mylist)

#intlist
#Iterates list usign loops to access each item and declare it
#does not allow you to change the list
intlist = [1,3,5,7,9]
for x in intlist:
    print (x)

#you can iterate by index that can change the list
for i in range (len(intlist)):
    intlist[i] = intlist[i] + 2.5
print (intlist)

#counters, variables that can keep getting added
sum = 0

for i in range (len(intlist)):
    sum += intlist [i]
print (sum)

#sorting in revsere
intlist.sort (reverse = True);
print(intlist)

#mylist 3
#sorting word list alphanumerical
mylist3 = ["dog", "snake", "cat", "gerbil", "bird"]
mylist3.sort ()
print(mylist3)

#list comprehension, 
#is doing the long way of doing a list
intlist = []
for i in range (10):
    intlist.append(i)
print(intlist)

#shorter way
intlist = [i for i in range (100)]
print (intlist)

#list inside of a list (double list)

allPeople = [ ["Elsy", 21], ["Paola", 24], ["Bianca", 21], ["Cat", 28]]
adults = [x for x in allPeople if x[1] > 21]
print (adults)

