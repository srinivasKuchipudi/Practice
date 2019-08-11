#Problem task: Create function which determines if it's a primary number and sum of all the digits is equal to 10

import string
import logging
import module_Prime_Identifier_Vinod as PI



#intializing logging object

logging.basicConfig(filename="isprime_log_Vinod.log",level=logging.DEBUG,filemode='w')
logger=logging.getLogger()


while (True):
    isPrime=""
    try:
        input_num=input("Enter a number:") #Reads the number
        while (True): # iterates till user enters a valid number
            if PI.iffloat(input_num)==True:
                logging.warning("Entered value "+ input_num + " is a decimal")
                input_num = input("Enter a valid integer number (>01) :")
            elif (int(input_num) <= 0):
                logging.warning("Entered value " + input_num + " is a negative value")
                input_num = input("Enter a valid number (>0) :")
            elif (input_num.isdigit() == False):
                logging.warning("Entered value " + input_num + " is a string")
                input_num = input("Enter a valid integer number (>0) :")

            else:
                break
        input_num = int(input_num)

        isPrime=PI.chkPrime(input_num)
    except Exception as e:
        print("An error occurred. Please check log for more details")
        logger.error("A run-time error occurred: " + str(e))
    if isPrime==True or isPrime==False:
        info_msg="Program ran successfully. Result: Prime and Sum to 10 for input "+ str(input_num) +" is "+str(isPrime)
        logger.info(info_msg)
    print(info_msg)
    # if(input_num==1):
    #     print(input_num, "is neither a prime nor a composite")
    # elif (isPrime==1):
    #     print(input_num,"is a prime")
    # else:
    #     print(input_num,"is not a prime")
    #
    #
    # sum=module_Prime_Identifier.chkto10(input_num)
    # if(sum<10):
    #     print(10-sum," more is/are required to get summed to 10")
    # elif (sum>10):
    #     print(sum-10,"'s is/are more to 10")
    # else:
    #     print("Yay!! The number is exactly equal to 10")


    while (True):
        contin = input("Would you like to continue? [Y/N]:")
        contin=contin.upper()
        if(contin in ('Y','N')):
            break
    if(contin=='N'):
        print("End of process!!")
        break