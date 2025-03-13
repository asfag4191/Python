from math import log


def solve_for_exp(a,b):
    #a**c=b, want to find c, use log
    return round(log(b,a))

import unittest

class TestSolveForExp(unittest.TestCase):
    def test_solve_for_exp(self):
        self.assertEqual(solve_for_exp(4, 1024), 5)
        self.assertEqual(solve_for_exp(2, 1024), 10)
        self.assertEqual(solve_for_exp(9, 3486784401), 10)
        self.assertEqual(solve_for_exp(4, 4294967296), 16)
        self.assertEqual(solve_for_exp(8, 134217728), 9)
        self.assertEqual(solve_for_exp(19, 47045881), 6)
        self.assertEqual(solve_for_exp(10, 100000000), 8)

if __name__ == "__main__":
    unittest.main()
