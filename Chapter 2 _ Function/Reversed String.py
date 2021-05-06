def reverse_string(str):  
    str1 = ""    
    for i in str:  
        str1 = i + str1  
    return str1      
     
str = input("Enter String:")           
print("The original string is: ",str)  
print("Reversed String",reverse_string(str)) 