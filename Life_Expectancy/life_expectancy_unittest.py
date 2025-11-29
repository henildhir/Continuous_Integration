import unittest
import os
from life_expectancy import plot_life_expectancy  

#This class will test for the life expectancy plot
class TestPlotLifeExpectancy(unittest.TestCase):

    #This function will test whether the plot has been created
    def test_plot_creates_files(self):
        saved_files = plot_life_expectancy()
        
        # Check that returned object is a list
        self.assertIsInstance(saved_files, list)

        # Check that at least one file path is returned
        self.assertTrue(len(saved_files) > 0)

        # Verify each file exists
        for file_path in saved_files:
            self.assertTrue(os.path.isfile(file_path), f"File does not exist: {file_path}")

if __name__ == "__main__":
    unittest.main()