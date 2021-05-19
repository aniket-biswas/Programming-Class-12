def palindrome(s): 
  s=s.upper()
  a=reversed(s)
  if list(s)==list(a):
    print("It's a Palindrome String")
  else:
    print("It's not a palindrome")
s=str(input("Enter string:"))
palindrome(s)
