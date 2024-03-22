import unittest
from src.multiply import multiply

class TestMultiply(unittest.TestCase):
    def test_multiply_failure(self):
        self.assertEqual(multiply(2, 3), 7)  # Ceci va échouer

if __name__ == '__main__':
    unittest.main()
