def maxlist():
    n=int(input("Enter the no of no's:"))
    l=[]
    for i in range(0,n):
        element=int(input("Enter no:"))
        l.append(element)
        a=sum(l)
    print(a)
maxlist()
