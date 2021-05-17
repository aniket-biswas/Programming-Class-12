def test_range(n):
    a=int(input("ENTER NO:"))
    b=int(input("ENTER NO:"))
    if n in range(a,b):
        print( " %s is in the range"%str(n))
    else :
        print("The number is outside the given range.")
n=int(input("ENTER NO YOU WANT TO SEARCH: "))
test_range(n)
