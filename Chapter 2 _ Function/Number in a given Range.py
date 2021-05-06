"""
def numbercheck(): 
  a=int(input("Enter Starting No="))
  b=int(input("Enter Ending No="))
  n=int(input("Enter No you want to search="))
  l=[]
  for i in range(a,b):
    l.append(i)
    
  
  
  if n in l:
    print(n," is present between",a,"and",b)
numbercheck()
"""


def test_range(n):
    a=int(input("ENTER NO:"))
    b=int(input("ENTER NO:"))
    if n in range(a,b):
        print( " %s is in the range"%str(n))
    else :
        print("The number is outside the given range.")
n=int(input("ENTER NO YOU WANT TO SEARCH: "))
test_range(n)