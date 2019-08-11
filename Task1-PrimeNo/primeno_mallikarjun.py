import math
import logging
import logging.config

def is_prime(val):
    count = 0
    if val <= 1:
        return False

    for i in range(2, math.floor(val / 2)):
        if (val % i) == 0:
            count = count + 1
            break

    if count > 0:
        #print(str(val) + " is not a prime number")
        return False
    else:
        return True


def number_sum(n):
    s = str(n)
    st = list(s)
    total = 0
    for c in st:
        # print(c + " ,")
        total = total + int(c)
    return total


def isPrime(val):

    msg = ""
    retFlag = False
    logging.basicConfig(filename='primeno_app_log.log',level=logging.DEBUG)
    logger = logging.getLogger()

    try:
        if isinstance(val, float):
            logger.warning(str(val) + " is a float, please enter a number")
            return False

        if val <= 1 or val == 2:
            return False

        prime_flag = is_prime(val)
        valStr = str(val)

        if prime_flag:
            print(valStr + " is a prime number")
            tot = number_sum(val)
            logging.info("total of " + str(val) + " is " + str(tot))
            if val < 10:
                msg = valStr + " is a prime but not equal to 10"
                retFlag = False
            else:
                tot = number_sum(val)
                if tot == 10:
                    msg = valStr + " is a prime and equal to 10"
                    retFlag = True
                else:
                    msg = valStr + " is a prime but not equal to 10"
                    retFlag = False
        else:
            msg = valStr + " is not a prime number"
            retFlag = False
            print(msg)

    except:
        logging.error('Unexpected error')

    logger.info(msg)

    return retFlag


'''
prime = input("Enter a number:")
if prime.isnumeric():
    is_prime = is_prime_n_equal_to_10(int(prime))
    print(is_prime)
else:
    print("Given input is not a number")
'''