# num = int(input("Enter a number: "))
# def prime(num):
#     if num > 1: # Prime no is always greater than 1
#     # checking for factors
#         for i in range(2,num):
#             if (num % i) == 0:
#                 print(num,"is not a prime number")
#                 print(i,"times",num//i,"is",num)
#                 break
#         else:
#             print(num,"is a prime number")
#     else:
#         print("The no is 1")
# prime(num)



def primeno(n):
    count=0
    i=1
    while(i<=n):
        if(n%i==0):
            count+=1
            print(i,"times",n//i,"is",n)
        i+=1
    if count==2:
        print("Prime No")
    else:
        print("Not a prime No:")
n= int(input("Enter a number: "))
primeno(n)





