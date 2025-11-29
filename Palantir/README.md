# Palantir Stock Price Analysis

This project provides tools to analyze the historical stock prices of Palantir Technologies. It includes data cleaning, calculation of daily percentage changes, and visualization of these metrics over time. Additionally, it evaluates the computational efficiency of sorting algorithms applied to the daily stock price changes.

## Features

- **Data Cleaning**: Reads and cleans Palantir stock data by removing irrelevant columns and converting date and price data to appropriate formats.
- **Visualization**:
  - Plots the closing price of the stock against dates.
  - Plots daily percentage change in stock price against dates.
- **Performance Analysis**: Computes and plots the time complexity of sorting daily price changes for varying input sizes, showcasing algorithmic efficiency with respect to data size.

## File Descriptions

### closing_price_function.py

- Loads historical Palantir stock data from `HistoricalData.csv`.
- Drops unnecessary columns such as 'Volume', 'Open', 'High', and 'Low'.
- Converts the 'Date' column to a datetime format and cleans the 'Close/Last' price column by removing dollar signs and converting it to float.
- Calculates the daily percentage change in the closing price.
- Generates a figure with two subplots:
  - Closing Price vs Date
  - Daily Percentage Change (%) vs Date
- Saves the plot as `Closing_price_vs_percentage_change.png` within the `Palantir` directory.

### daily_price_change.py

- Contains the function `calculate_daily_changes(df, max_days=365, step=7)` which:
  - Calculates daily changes in stock price over increasing data sizes.
  - Measures the time taken to sort these daily changes for each data size.
  - Plots time taken to sort against input size.
  - Compares observed sorting time to the theoretical O(n log n) time complexity by scaling and plotting both on the same graph.
- Saves the output plot as `Daily_price_change.png` in the `Palantir` directory.

### Unittest.py

- Contains unit tests (not shown here) designed to verify the correctness and robustness of the data processing and analysis functions.
- Tests ensure data cleaning, percentage change calculations, and plotting functions behave as expected.
- Helps maintain code reliability when changes are introduced.