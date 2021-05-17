import math
print("PLEASE INPUT POSITIVE NATURAL NUMBERS ONLY")
def fact(n):
    a=math.factorial(n)
    print("Factorial of",n,"is",a)
n=int(input("Enter No:"))
fact(n)
