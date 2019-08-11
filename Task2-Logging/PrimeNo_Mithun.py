from Logger_Mithun import logger

def isPrime(b):
    primeNo = b
    try:
        if isinstance(b, float):
            logger().warn("Input number " + str(primeNo) + " is float")
        if b > 1:
            for i in range(2, b//2):
                if b%i==0:
                    logger().error("Number " + str(primeNo) + " is not prime")
                    return False
        else:
            logger().error("Number " + str(primeNo) + " is not prime since its lesser than 1")
            return False

        integerSum = 0
        while b>0 and integerSum!=10:
            integerSum += int(b%10)
            b = int(b/10)

        if integerSum==10:
            logger().info("Number " + str(primeNo) + " is prime and sum is 10")
            return True
        else:
            logger().error("Number " + str(primeNo) + " is prime but sum of its digits is not 10")
            return False
    except Exception as err:
        logger().error("Error: " + str(err))