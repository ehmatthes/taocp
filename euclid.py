def get_gcd(x, y):
    """Calculate the greatest common divisor of two numbers."""
    if y > x:
        x, y = y, x

    r = x % y
    if r == 0:
        return y
    else:
        result = get_gcd(y, r)

    return result
        

# Test the function.
import unittest

class TestEuclid(unittest.TestCase):
    def test(self):
        self.assertEqual(get_gcd(100, 75), 25)
        self.assertEqual(get_gcd(75, 100), 25)
        self.assertEqual(get_gcd(544, 119), 17)
        self.assertEqual(get_gcd(119, 544), 17)

unittest.main()
