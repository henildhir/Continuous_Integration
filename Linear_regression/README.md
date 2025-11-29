# Linear Regression Data Generation and Testing

## Overview

This project demonstrates how to generate synthetic linear data with noise, perform linear regression on the data, and validate the results using unit tests.

---

## Files and Structure

- `Data_function.py`  
  Contains the `generate_data_graph` function which:
  - Creates synthetic data points following a linear equation `y = mx + b` plus Gaussian noise.
  - Saves the generated data to a CSV file.
  - Performs linear regression on the generated data.
  - Saves a scatter plot with the original data, true line, and fitted regression line as an image.

- `Unit_Test.py`  
  Contains unit tests that verify the correctness of the `generate_data_graph` function's output:
  - Validates the slope estimation.
  - Validates the intercept estimation.
  - Uses Python's `unittest` framework for automated testing.

- `data.csv`  
  CSV file containing the generated synthetic data points (x and y).

- `plot.png`  
  PNG image file of the generated plot showing data points and regression lines.

---

## How to Use

1. **Generate Data and Plot**

   Run the script `Data_function.py` to generate data, perform linear regression, and save the results:

   ```bash
   python Data_function.py