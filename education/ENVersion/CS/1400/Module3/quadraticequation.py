#How to get the quadratic equation
#x=-b+-√b^2-4ac/2A
import math
#title
print ("Quadratic Formula")
#values of quad
a=float (input("Enter the value for a: "))
b=float (input("Enter the value for b: "))
c=float (input("Enter the value for c: "))
#formula
x1 = (-b + math.sqrt( math.pow(b,2) - 4*a*c)) / (2*a)
x2 = (-b - math.sqrt( math.pow(b,2) - 4*a*c)) / (2*a)
#solution
print ("The solution are:", x1,"or", x2)