import unittest
from my_function import multiply

# define the unit tests
class my_unit_tests(unittest.TestCase):
    def test_add(self):

        # test adding negative integers
        self.assertEqual(multiply(4,5),20)

        # test adding floats"
        self.assertEqual(multiply(3,2),7)

# run the tests
if __name__ == "__main__":
    unittest.main()