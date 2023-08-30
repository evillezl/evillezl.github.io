import random

slot1 = random.randrange(1, 3)
slot2 = random.randrange(1, 3)
slot3 = random.randrange(1, 3)
num = 50
end = 0
start = input("Welcome to Elsy's Slot Machine! You will start with $50. Will you stake money to play? Y/N:")
end = int(input("How much money do you want to stake?"))

while start == "y" or start == "Y":
    while slot1 != 1 and slot3 != 4:
        slot1 = random.randrange(1, 3+1)
        slot2 = random.randrange(1, 3+1)
        slot3 = random.randrange(1, 3+1)
    if slot1 == 1 and slot2 == 1 and slot3 == 1:
        print ("Win")
        num += end
    elif slot1 == 2 and slot2 == 2 and slot3 == 2:
        print ("Win")
        num += end
    elif slot1 == 3 and slot2 == 3 and slot3 == 3:
        print ("Win")
        num += end
    else:
        print("Lose")
        num -= end
    print(slot1, slot2, slot3)
    start = input("Will you stake money to play? Y/N:")
    end = int(input("How much money do you want to stake? If said N write 0:"))
print ("You went home with",num,"dollars.")


