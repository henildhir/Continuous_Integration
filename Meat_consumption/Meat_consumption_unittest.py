import unittest
import pandas as pd

from meat_consumption_function import plot_meat_vs_population

class TestMeatConsumptionData(unittest.TestCase):

    def setUp(self):
        self.meat_csv_path = 'Meat_consumption/global-meat-projections-to-2050.csv'
        self.pop_csv_path = 'Meat_consumption/population-with-un-projections.csv'
        self.meat_df = pd.read_csv(self.meat_csv_path)
        self.pop_df = pd.read_csv(self.pop_csv_path)

    def test_meat_dataframe_columns(self):
        expected_columns = {'Entity', 'Year', 'Beef and Buffalo', 'Pigmeat', 'Sheep and goat', 'Poultry'}
        missing = expected_columns - set(self.meat_df.columns)
        self.assertFalse(missing, f"Missing columns in meat data: {missing}")

    def test_population_dataframe_columns(self):
        expected_columns = {
            'Entity', 
            'Year', 
            'Population - Sex: all - Age: all - Variant: estimates'
        }
        missing = expected_columns - set(self.pop_df.columns)
        self.assertFalse(missing, f"Missing columns in population data: {missing}")

if __name__ == '__main__':
    unittest.main()