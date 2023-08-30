#Tip Caculator

#Allows the user to enter the cost of the meal

#Allows the user to enter the service excellent, good, poor

#caculator total cost of the meal

print ("Tip Caculator")
cost = float(input("Enter the cost of your meal:"))
service = input("How was the service? Excellent, Good, Poor:")
percentage = .15
if service == "Excellent" or service == "excellent":
    percentage += .05
elif service == "Good" or service == "good":
        percentage += .03
elif service == "Poor" or service == "poor":
        percentage -= .05       
    
tip = round(cost * percentage, 2)
cost += tip 
print("Tip:", tip)
print ("Cost:", cost)