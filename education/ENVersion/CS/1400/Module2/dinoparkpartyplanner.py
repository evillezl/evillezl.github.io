print ("Dinosaur Park Party Caculator")
cost = 0
question1 = input("Which package would you like to know the cost of? A. Bare Bones B. Deluxe Party C. Group Rate Admission Party D. -1 to Quit:")
while question1 == "A" or question1 == "a" or question1 == "Bare Bones" or question1 == "A. Bare Bones" or question1 == "bare bones" or question1 == "B" or question1 == "b" or question1 == "Deluxe" or question1 == "B. Deluxe Party" or question1 == "deluxe" or question1 == "C" or question1 == "c" or question1 == "Group Rate Admission" or question1 == "C. Group Rate Admission Party" or question1 == "group rate admission":
    
    while question1 == "A" or question1 == "a" or question1 == "Bare Bones" or question1 == "A. Bare Bones" or question1 == "bare bones":
        print ('Great! Bare Bones Package includes admission up to 12 people, and child receives a 2-3" geode.')
        question2 = input("Do you have membership with the Dinosaur Park? Y/N:")
        if question2 == "Y" or question2 == "y":
            cost += 99
        elif question2 == "N" or question2 == "n": 
            cost += 119
        num = int(input("For each addition child or adult it is $3, How many additional people are you going to have?"))
        cost += num*3
        print ("Total cost of the party:", cost)
        question1 = input("Which package would you like to know the cost of? A. Bare Bones B. Deluxe Party C. Group Rate Admission Party D. -1 to Quit:")

    while question1 == "B" or question1 == "b" or question1 == "Deluxe" or question1 == "B. Deluxe Party" or question1 == "deluxe":
        print ('Great! Deluxe Package includes admission up to 12 people, child receives a 3-4" geode, scavenger hunt book, 20 min tour and fossil casting.')  
        question2 = input("Do you have membership with the Dinosaur Park? Y/N:")
        if question2 == "Y" or question2 == "y":
            cost += 175
        elif question2 == "N" or question2 == "n": 
            cost += 199
        num = int(input("For each addition child or adult it is $3, How many additional people are you going to have?"))
        cost += num*3
        print ("Total cost of the party:", cost)
        question1 = input("Which package would you like to know the cost of? A. Bare Bones B. Deluxe Party C. Group Rate Admission Party D. -1 to Quit:")

    while question1 == "C" or question1 == "c" or question1 == "Group Rate Admission" or question1 == "C. Group Rate Admission Party" or question1 == "group rate admission":
        print ('Great! By reserving a group party slot of 10 or more people and with 7 day notice your group will be admitted through a discounted rate.')   
        num = int(input("How many adults?"))
        cost += num*5
        num = int(input("How many children?"))
        cost += num*4
        print ("Total cost of the party:", cost)
        question1 = input("Which package would you like to know the cost of? A. Bare Bones B. Deluxe Party C. Group Rate Admission Party D. -1 to Quit:")
