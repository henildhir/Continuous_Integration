import unittest
import os
import sys
import numpy as np
import pandas as pd

from daily_price_change import calculate_daily_changes, save_dir  # Adjust import as needed

class TestDailyPriceChange(unittest.TestCase):

    def setUp(self):
        # Verify that the data file exists before running tests
        self.file_path = 'Palantir/HistoricalData.csv'
        self.assertTrue(os.path.isfile(self.file_path), f"Data file not found: {self.file_path}")

        # Load the CSV data into a DataFrame
        self.df = pd.read_csv(self.file_path)

    def test_data_integrity(self):
        # Check that there are no missing values in the DataFrame
        self.assertFalse(self.df.isnull().values.any(), "Data contains missing values")

        # Ensure that the required columns 'Date' and 'Close/Last' are present
        for col in ['Date', 'Close/Last']:
            self.assertIn(col, self.df.columns, f"Required column missing: {col}")

    def test_sorting_output(self):
        # Clean the 'Close/Last' column by removing '$' and converting to float, as in the main function
        self.df['Close/Last'] = self.df['Close/Last'].str.replace('$', '', regex=False).astype(float)

        # Sort the DataFrame by 'Date' to ensure chronological order
        self.df = self.df.sort_values('Date')

        # Run the function to get sorting results
        n_values, time_values = calculate_daily_changes(self.df, max_days=30, step=5)

        # Check that the outputs are numpy arrays
        self.assertIsInstance(n_values, np.ndarray, "'n_values' should be a numpy ndarray")
        self.assertIsInstance(time_values, np.ndarray, "'time_values' should be a numpy ndarray")

        # Verify that both arrays have the same length
        self.assertEqual(len(n_values), len(time_values), "Output arrays must be the same length")

        # Ensure that the arrays are not empty (function actually performed sorting)
        self.assertGreater(len(n_values), 0, "Output arrays are empty, sorting may not have executed")

if __name__ == '__main__':
    unittest.main()