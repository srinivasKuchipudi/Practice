import unittest

from PrimeNo_Mithun import isPrime
from Logger_Mithun import logger


class PrimeNoTest(unittest.TestCase):


    def setUp(self):
        pass
    def testcheckZero(self):
        try:
            print('test')
            self.assertEqual( isPrime(2.3), False)
        except AssertionError as err:
            logger().error("Assertion failure for testcheckzero : " + str(err))

    def testNum181(self):
        try:
            print('test')
            self.assertEqual( isPrime(181), True)
        except AssertionError as err:
            logger().error("Assertion failure for testNum181 : " + str(err))

    def testNum180(self):
        try:
            print('test')
            self.assertEqual( isPrime(180), False)
        except AssertionError as err:
            logger().error("Assertion failure for testNum180 : " + str(err))
if __name__ == '__main__': 
    unittest.main()