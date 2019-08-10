
# Function to validate prime
def chkPrime(num):
    flag_prime = 1

    for i in range(2, int(num / 2)+1):
        if (int(num % i) == 0):
            flag_prime = 0
            break
    #print(flag_prime)
    sum=chkto10(num)
    #print(sum)
    if (sum ==10 and flag_prime ==1):
        return True
    else:
        return False

# Function to check to 10
def chkto10(num):
    sum1=0
    #str_num=str(num)
    str_input_num = [int(d) for d in str(num)]
    for i in range(0, len(str_input_num)):
        sum1 += int(str_input_num[i])
    return sum1

def iffloat(num):
    if num.isdigit() == True or int(num) < 0:
        return False
    try:
       is_float=float(num)
    except ValueError:
        return False
    return True