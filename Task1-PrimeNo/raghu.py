
# Function to validate prime
def chkPrime(num):
    flag_prime = 1

    for i in range(2, int(num / 2)+1):
        if (int(num % i) == 0):
            flag_prime = 0
            break
    return  flag_prime

# Function to check to 10
def chkto10(num):
    sum=0
    str_input_num = [int(d) for d in str(num)]
    for i in range(0, len(str_input_num)):
        sum += int(str_input_num[i])
    return sum


@@ -0,0 +1,41 @@
#Problem task: Create function which determines if it's a primary number and sum of all the digits is equal to 10

import string

while (True):
    input_num=input("Enter a number:") #Reads the number
    while (True): # iterates till user enters a valid number
        if (input_num.isdigit() == False):
            input_num = input("Enter a valid integer number (>0) :")
        elif(int(input_num)<=0):
            input_num = input("Enter a valid number (>0) :")
        else:
            break
    input_num = int(input_num)
    isPrime=chkPrime(input_num)

    if(input_num==1):
        print(input_num, "is neither a prime nor a composite")
    elif (isPrime==1):
        print(input_num,"is a prime")
    else:
        print(input_num,"is not a prime")


    sum=chkto10(input_num)
    if(sum<10):
        print(10-sum," more is/are required to get summed to 10")
    elif (sum>10):
        print(sum-10,"'s is/are more to 10")
    else:
        print("Yay!! The number is exactly equal to 10")

    while (True):
        contin = input("Would you like to continue? [Y/N]:")
        contin=contin.upper()
        if(contin in ('Y','N')):
            break
    if(contin=='N'):
        print("End of process!!")
        break