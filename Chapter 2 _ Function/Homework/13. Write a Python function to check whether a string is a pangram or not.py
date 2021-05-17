def pangram(): # Pangram--> Contains all alpahbets A-Z and a-z 
  import string
  inputString = input("Enter the string : ")
  lcase = inputString.lower()
  lcase = lcase.replace(" ","")
  inputStringList = set(lcase)
  if len(inputStringList) == 26 :
    print("This is a pangram string")
  else:
    print("This is not a pangram string")
pangram()