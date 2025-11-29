# US Election Data Analysis

This folder contains scripts and data related to the analysis and visualization of the 2016 US Primary election results. The main focus is to provide insights into the distribution of votes received by different candidates across US states.

## Contents

- `US-2016-Primary.csv`: Dataset containing primary election results with fractional vote counts by candidate and state.
- `US_Election_graph.py`: Python script that processes the election data and generates a bar plot showing the distribution of fraction of votes for a specified candidate across states.
- `US_Election_unittest.py`: Unit test script to verify the correctness of the main election graph function.

## Description

### US_Election_graph.py

- Reads the election data CSV file.
- Prompts the user to enter a candidate's name.
- Filters the data for the chosen candidate.
- Aggregates the fraction of votes per state.
- Plots a bar graph showing how the candidate’s fraction of votes is distributed across all states.
- Displays the plot and returns the aggregated vote data as a pandas Series.

### US_Election_unittest.py

- Contains unit tests for validating the election graph functionality.
- Tests that the aggregated vote data:
  - Is a non-empty pandas Series,
  - Contains expected states such as 'California',
  - Has a total sum greater than zero, ensuring meaningful data.

## How to run the code

1. Ensure the dataset `US-2016-Primary.csv` is in the `US_Election` folder.
2. Run `US_Election_graph.py`. When prompted, enter a candidate’s name (case insensitive).
3. A bar graph of vote distribution across states will be displayed.
4. Run `US_Election_unittest.py` to execute unit tests verifying the data processing logic.