#This unit test will test for both  slope and intercept and whether the values returned are approximately equal to the expected slope 

import unittest
from Data_function import generate_data_graph  

#This class will test for each slope and intercept
class TestGenerateDataGraph(unittest.TestCase):

    #The function will test for the slope and whether the gradient is equal to 2. In this case the grade may not be equal to 2 hence the test has failed
    def test_slope(self):
        slope, intercept = generate_data_graph(m=2.0, b=1.0, noise_std=0.1, n_points=100)
        self.assertEqual(slope, 2.0, places=1)

    ##The function will test for the slope and whether the gradient is equal to 1. In this case the grade may be approximately equal to 1 hence the test has passed
    def test_intercept(self):
        slope, intercept = generate_data_graph(m=2.0, b=1.0, noise_std=0.1, n_points=100)
        self.assertAlmostEqual(intercept, 1.0, places=1)

if __name__ == "__main__":
    unittest.main()