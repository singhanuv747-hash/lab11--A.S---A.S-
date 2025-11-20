# https://github.com/singhanuv747-hash/lab11--A.S---A.S-.git
# Partner 1: <Anuv Singh>
# Partner 2: None

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):

    # Partner 2
    def test_add(self):
        self.assertEqual(add(3, 4), 7)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(sub(10, 3), 7)
        self.assertEqual(sub(0, 5), -5)
        self.assertEqual(sub(-5, -5), 0)

    # Partner 1
    def test_multiply(self):
        self.assertEqual(mul(3, 4), 12)
        self.assertEqual(mul(0, 5), 0)
        self.assertEqual(mul(-2, 3), -6)

    def test_divide(self):
        self.assertEqual(div(10, 2), 5)
        self.assertEqual(div(-9, 3), -3)
        self.assertEqual(div(5, 1), 5)

    # Partner 2
    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(5, 0)

    def test_logarithm(self):
        self.assertEqual(log(8, 2), 3)
        self.assertAlmostEqual(log(100, 10), 2)
        self.assertAlmostEqual(log(27, 3), 3)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            log(10, 1)

    # Partner 1
    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            log(-5, 2)

    def test_hypotenuse(self):
        # You do NOT have a hypotenuse function, so comment these out
        pass

    def test_sqrt(self):
        # You do NOT have a sqrt function, so comment these out
        pass

# Do not touch this
if __name__ == "__main__":
    unittest.main()
