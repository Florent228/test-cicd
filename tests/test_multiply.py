import unittest
from src.multiply import multiply

class TestMultiply(unittest.TestCase):
    def test_multiply_success(self):
        self.assertEqual(multiply(2, 3), 6)  # Correction pour réussir

if __name__ == '__main__':
    unittest.main()
