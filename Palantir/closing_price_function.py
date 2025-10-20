import numpy as np
import pandas as pd

palantir_df = pd.read_csv('Palantir/HistoricalData.csv')  # replace with your actual file path

columns_to_drop = ['Volume', 'Open', 'High', 'Low']
palantir_df = palantir_df.drop(columns=columns_to_drop)

# Check the result
print(palantir_df.head())