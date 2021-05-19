import math
def product(n):
    l=[]
    for i in range(0,n):
        element=int(input("Enter no:"))
        l.append(element)
        sum=math.prod(l)
    print(l)
    print(sum)
n=int(input("Enter the no of no's:"))
product(n)
    