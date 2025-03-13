def factorial(num):
    result=1 #starte på 1, siden kan ikke mutliplisere med 0
    for i in range(1,num+1):#passe på å gå gjennom alle tallene, og igjen starte på 1
        result=result*i
    return result

import unittest

class TestFactorial(unittest.TestCase):
    def test_factorial(self):
        self.assertEqual(factorial(2), 2)
        self.assertEqual(factorial(6), 720)
        self.assertEqual(factorial(3), 6)
        self.assertEqual(factorial(12), 479001600)
        self.assertEqual(factorial(5), 120)

if __name__ == "__main__":
    unittest.main()
