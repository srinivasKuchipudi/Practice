import math


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
    if val <= 1 or val == 2:
        return False

    prime_flag = is_prime(val)

    if prime_flag:
        print(str(val) + " is a prime number")
        tot = number_sum(val)
        print("total of " + str(val) + " is " + str(tot))
        if val < 10:
            return False
        else:
            tot = number_sum(val)
            if tot == 10:
                return True
            else:
                return False
    else:
        print(str(val) + " is not a prime number")
        return False


'''
prime = input("Enter a number:")
if prime.isnumeric():
    is_prime = is_prime_n_equal_to_10(int(prime))
    print(is_prime)
else:
    print("Given input is not a number")
'''