# Global Meat Consumption and Population Analysis

This project analyses global meat consumption trends in relation to population growth using historical data. It processes and visualises meat consumption data alongside world population figures to provide insights into how meat demand has evolved over time.

## Overview

The analysis focuses on meat consumption from 1961 to 1965 (configurable within the code) and compares it with the corresponding world population data. Key meat types such as beef, pigmeat, sheep and goat, and poultry are aggregated to calculate total meat consumption. The combined dataset enables the exploration of trends and relationships between meat consumption and population growth.

## Data Sources

- **Meat Consumption Data**: Includes annual consumption volumes of various meat types by country and year.
- **Population Data**: Contains population estimates segmented by country and year.

Both datasets are filtered to include only global data ("World" entity) for the chosen time span.

## Functionality

- **Data Cleaning and Aggregation**: Filters relevant years and entities, sums meat types to compute total meat consumption.
- **Data Merging**: Combines the population and meat consumption data on the year field for joint analysis.
- **Visualisation**: Generates a dual-axis plot showing:
  - Total meat consumption in million tons (left y-axis)
  - World population in billions (right y-axis)
  
This visualisation highlights the interplay between population growth and meat demand over the selected years.

## Output

- A clear, concise graph titled *"Global Meat Consumption vs Population (1990-2013)"* is generated.
- The plot is saved to the `Meat_Consumption` directory for further review and reporting.

## Usage

- Make sure the datasets (`global-meat-projections-to-2050.csv` and `population-with-un-projections.csv`) are placed in the correct folders as indicated in the code.
- Run the plotting script `meat_consumption_function.py` to create and save the visualisation.
- Modify filtering years or entities in the script as needed to expand or narrow the analysis window.
