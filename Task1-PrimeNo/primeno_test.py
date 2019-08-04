import unittest
from primeno_mallikarjun import isPrime


class PrimeNoTest(unittest.TestCase):
    def setUp(self):
        pass

    def testcheckZero(self):
        print('test')
        self.assertEqual(isPrime(0), False)

    def testNum181(self):
        print('test')
        self.assertEqual(isPrime(181), True)

    def testNum180(self):
        print('test')
        self.assertEqual(isPrime(180), False)

    def testNum19(self):
        print('test')
        self.assertEqual(isPrime(19), True)


if __name__ == '__main__':
    unittest.main()