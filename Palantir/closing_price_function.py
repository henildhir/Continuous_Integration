import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#This cleans the data and drops unnecessary columns
palantir_df = pd.read_csv('Palantir/HistoricalData.csv')  # replace with your actual file path
columns_to_drop = ['Volume', 'Open', 'High', 'Low']
palantir_df = palantir_df.drop(columns=columns_to_drop)

#Changes the Date column from a string to DateTime format
palantir_df['Date'] = pd.to_datetime(palantir_df['Date'])
#Converts the closing price to a string to remove the '$' symbol
palantir_df['Close/Last'] = palantir_df['Close/Last'].str.replace('$','',regex=False).astype(float)
#Calculates daily percentage change between days
palantir_df['Daily_Percentage_Change'] = palantir_df['Close/Last'].pct_change()*100

#Creates a figure with 2 plots with the same figure size
fig,(ax1,ax2) = plt.subplots(1,2,figsize=(15,6),sharex=True)

#Plots Closing price against date with all axis labelled
ax1.plot(palantir_df['Date'],palantir_df['Close/Last'],marker='o')
ax1.set_ylabel('Closing Price ($)')
ax1.set_title('Palantir Closing Price vs Date')
ax1.set_xlabel('Date')
ax1.tick_params(axis='x',rotation=45)

#Plots Daily percentage change against date with all axis labelled
ax2.plot(palantir_df['Date'],palantir_df['Daily_Percentage_Change'],marker='o',color='red')
ax2.set_xlabel('Date')
ax2.set_ylabel('Daily Percentage Change (%)')
ax2.set_title('Daily Percentage Change vs Date')
ax2.tick_params(axis='x',rotation=45)

plt.tight_layout()
plt.show()

# Check the result
#print(palantir_df.head())
