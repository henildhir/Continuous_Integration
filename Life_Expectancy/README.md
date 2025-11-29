# Life Expectancy Polynomial Forecast

This project analyzes historical life expectancy data for selected countries and generates polynomial regression models to visualize past trends and forecast future life expectancy.

## Overview of the Code

The core functionality is implemented in the `plot_life_expectancy()` function. This function performs the following steps:

- Loads life expectancy data from a CSV file, cleaning column headers and converting the 'Year' column to numeric values.  
- Filters the dataset for three countries: United Kingdom, India, and Malawi, focusing on data between 1950 and 2015.  
- For each country:
  - Extracts the relevant yearly life expectancy data.
  - Fits polynomial models of degree 1 through 9 to the data.
  - Creates a plot combining the historical data points with polynomial fits and a 10-year forecast.
  - Saves each plot as a PNG file named `<Country>_polynomial_forecast.png` in the `Life_Expectancy` directory.
  - Displays each plot for user visualization.

This comprehensive approach allows for visual comparison of model fits at different polynomial degrees and provides insight into expected life expectancy trends in the near future.

## Purpose of the Unit Test

The accompanying unit test script `life_expectancy_unittest.py` verifies the functionality of the `plot_life_expectancy()` function with the following goals:

- **File Generation Verification**: Confirms that the function returns a list of saved plot file paths. This ensures that the plotting and saving mechanisms are executed as expected.  
- **File Existence Validation**: Iterates through all returned file paths and checks if those files actually exist on disk. This acts as a safeguard against silent failures in saving the plot images.  
- **Output Type Checking**: Verifies the type of the returned object to be a list, ensuring correct function behavior and easier integration with other components.  

In summary, the unit test ensures that the main plotting functionality processes the input data correctly, generates and saves plot images for each country, and produces a consistent and verifiable output. It does not test the visual correctness of the plots but effectively guarantees that the graph generation pipeline completes without errors and produces tangible output files.