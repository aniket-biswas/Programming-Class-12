num = int(input("Enter a number: "))
def prime(num):
    if num > 1: # Prime no is always greater than 1
    # checking for factors
        for i in range(2,num):
            if (num % i) == 0:
                print(num,"is not a prime number")
                print(i,"times",num//i,"is",num)
                break
        else:
            print(num,"is a prime number")
    else:
        print(num,"is not a prime number")
prime(num)