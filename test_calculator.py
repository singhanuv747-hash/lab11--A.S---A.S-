# https://github.com/singhanuv747-hash/lab11--A.S---A.S-.git
# Partner 1: <Anuv Singh>
# Partner 2: None

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):

    # Partner 1 tests you must complete
    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(0, 5), 0)
        self.assertEqual(multiply(-2, 3), -6)

    def test_divide(self):
        self.assertEqual(divide(2, 10), 5)  
        self.assertEqual(divide(5, 25), 5)
        self.assertEqual(divide(-1, 5), -5)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(-3, 2)

    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(3, 4), 5)
        self.assertAlmostEqual(hypotenuse(5, 12), 13)
        self.assertAlmostEqual(hypotenuse(1, 1), math.sqrt(2))

    def test_sqrt(self):
        with self.assertRaises(ValueError):
            square_root(-1)
        self.assertEqual(square_root(0), 0)
        self.assertEqual(square_root(9), 3)

# Do not touch this
if __name__ == "__main__":
    unittest.main()
