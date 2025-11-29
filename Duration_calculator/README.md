# Duration Calculator - Unit Tests

## Overview

This folder contains the **unit tests** and the underlying code for a duration calculator function. The main purpose of this project is to calculate the number of days left from today's date to a user-provided input date.

---

## Contents

- `duration_calculator.py`  
  Contains the `days_left` function, which takes a date string input (in `YYYY-MM-DD` format), converts it to a `datetime` object, and calculates the difference in days from today.

- `test_duration_calculator.py` (or your test file)  
  Contains the `unittest` test cases to verify the correctness of the `days_left` function using different date scenarios.

---

## Functionality

### `days_left(user_input)`

- **Input:**  
  A date string in the format `YYYY-MM-DD`.

- **Output:**  
  Returns a `numpy.timedelta64` object representing the difference in days between the input date and today's date. Positive if in the future, zero if today, negative if in the past.

- The function internally converts the string input into a NumPy datetime64 object and calculates the difference against today's date.

---

## Unit Tests

The unit tests verify that the `days_left` function behaves as expected under various conditions:

1. **Test with a past date:**  
   Ensures the function returns a negative difference for dates before today.

2. **Test with today's date:**  
   Ensures the function returns zero when the date is today's date.

3. **Test with a future date:**  
   Ensures the function returns a positive difference when the date is in the future.

The tests use Python's built-in `unittest` framework and the `numpy` library to validate outputs with assertions.
