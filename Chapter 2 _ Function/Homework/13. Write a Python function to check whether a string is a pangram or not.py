def pangram(string1): # Pangram--> Contains all alpahbets A-Z and a-z 
  import string
  
  lcase = string1.lower()
  lcase = lcase.replace(" ","")
  string1List = set(lcase)
  if len(string1List) == 26 :
    print("This is a pangram string")
  else:
    print("This is not a pangram string")
string1 = input("Enter the string : ")
pangram(string1)