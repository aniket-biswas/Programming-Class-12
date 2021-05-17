l=[]
def unique_list(l):
    n=int(input("Enter the no of no's:"))
    
    for i in range(0,n):
        element=int(input("Enter no:"))
        l.append(element)
    x = []
    for a in l:
        if a not in x:
            x.append(a)
    return x
print(unique_list(l)) 