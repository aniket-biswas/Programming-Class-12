import math
print("PLEASE INPUT POSITIVE NATURAL NUMBERS ONLY")
def fact(n):
    a=math.factorial(n)
    print(n,"!=",a)
n=int(input("Enter No:"))
fact(n)
