import unittest
import numpy as np
from functions.duration_calculator import days_left

class TestDaysLeft(unittest.TestCase):

    def test_past_date(self):
        #Date in the past - difference should be negative
        past_date='2000-01-01'
        expected_days = (np.datetime64(past_date) - np.datetime64('today')).astype(int)
        actual_days = days_left(past_date).astype(int)
        self.assertEqual(actual_days,expected_days)

if __name__ == "__main__":
    unittest.main()