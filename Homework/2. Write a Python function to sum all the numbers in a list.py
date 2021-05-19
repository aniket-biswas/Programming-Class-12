def sumlist(n):
    l=[]
    for i in range(0,n):
        element=int(input("Enter element:"))
        l.append(element)
        a=sum(l)
    print(a)
    print(l)
n=int(input("Enter the no of elements:"))
sumlist(n)

