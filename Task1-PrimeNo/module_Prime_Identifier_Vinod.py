
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
