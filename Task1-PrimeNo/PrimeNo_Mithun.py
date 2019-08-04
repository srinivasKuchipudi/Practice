def isPrime(b):
    if b > 1:
        for i in range(2, b//2):
            if b%i==0:
                return False
    else:
        return False

    integerSum = 0
    while b>0 and integerSum!=10:
        integerSum += int(b%10)
        b = int(b/10)

    if integerSum==10:
        return True
    else:
        return False