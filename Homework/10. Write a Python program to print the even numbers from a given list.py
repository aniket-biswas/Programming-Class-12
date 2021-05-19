def even(a,b):  
  print("!Important Message!")
  print("# If you want odd no please input 1st no as Odd #")
  print("# If you want even no please input 1st no as even #")
 
  if a == b:
    print("!Invalid! **Both the values are Same**")
  for i in range(a,b+1,2):
    print(i)
a=int(input("Enter Starting No="))
b=int(input("Enter Ending No="))
even(a,b)
      