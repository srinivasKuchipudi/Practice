import unittest
from primeno_mallikarjun import isPrime


class PrimeNoTest(unittest.TestCase):
    def setUp(self):
        pass

    def testcheckZero(self):
        print('testcheckZero')
        self.assertEqual(isPrime(0), False)

    def testNum181(self):
        print('testNum181')
        self.assertEqual(isPrime(181), True)

    def testNum180(self):
        print('testNum180')
        self.assertEqual(isPrime(180), False)

    def testNum19(self):
        print('testNum19')
        self.assertEqual(isPrime(19), True)

    def testFloat(self):
        print('testFloat14.5')
        self.assertEqual(isPrime(14.5), False)


if __name__ == '__main__':
    unittest.main()