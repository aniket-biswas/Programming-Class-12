def palindrome(): 
  s=str(input("Enter string:"))
  s=s.upper()
  a=reversed(s)
  if list(s)==list(a):
    print("palindrome")
  else:
    print("not palindrome")
palindrome()