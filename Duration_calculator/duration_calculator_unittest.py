import unittest
import numpy as np
from Duration_calculator.duration_calculator import days_left

class TestDaysLeft(unittest.TestCase):

    def test_past_date(self):
        #Date in the past - difference should be negative
        past_date='2000-01-01'
        #This will calculated the expected days left by subtracting past date and todays date

        expected_days = (np.datetime64(past_date) - np.datetime64('today')).astype(int)
        actual_days = days_left(past_date).astype(int)

        #This will check whether both calculated days using the function are the same 
        self.assertEqual(actual_days,expected_days)

    #this function will check whether the days left are 0 as it takes into account todays date only
    def test_today_date(self):
        today_date = str(np.datetime64('today'))
        self.assertEqual(days_left(today_date).astype(int),0)

    #this function will test whether the number of days remaining is positive. If it's negative, the test will fail
    def test_future_date(self):
        future_date = str(np.datetime64('today') + np.timedelta64(10, 'D'))
        self.assertEqual(days_left(future_date).astype(int),-10)

if __name__ == "__main__":
    unittest.main()