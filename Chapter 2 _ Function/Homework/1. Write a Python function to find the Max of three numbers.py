def maximum(a,b,c):
    
    if a>b>c:
        return a
    elif a>c>b:
        return a
    elif b>a>c:
        return b
    elif b>c>a:
        return b
    elif c>a>b:
        return c
    elif c>b>a:
        return c
    else:
        print("!Invalid!")
a=float(input("Enter 1st no="))
b=float(input("Enter 2nd no="))
c=float(input("Enter 3rd no="))
maximum(a,b,c)
s=max(a,b,c)
print(s)