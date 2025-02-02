import unittest

def add_numbers(a, b):
    """Add two numbers and return the result."""
    return a + b

class TestAddNumbers(unittest.TestCase):
    def test_add_positive_numbers(self):
        """Test the addition of two positive numbers."""
        self.assertEqual(add_numbers(3, 5), 8)

    def test_add_negative_numbers(self):
        """Test the addition of two negative numbers."""
        self.assertEqual(add_numbers(-3, -5), -8)

    def test_add_positive_and_negative_numbers(self):
        """Test the addition of a positive number and a negative number."""
        self.assertEqual(add_numbers(-5, 5), 0)

    def test_add_zero(self):
        """Test the addition of zero, which should not change the number."""
        self.assertEqual(add_numbers(0, 7), 7)
        self.assertEqual(add_numbers(0, 0), 0)

if __name__ == "__main__":
    unittest.main()
