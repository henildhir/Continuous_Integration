import time
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

#This will ensure that the plot is saved within this directory
save_dir="Palantir"

#Function to calculate the daily changes of stock price of Palantir
def calculate_daily_changes(df, max_days=365, step=7):

    #Empty list for n_values and time_values - initialise
    n_values = []
    time_values = []

    data_length = min(len(df),max_days)

    #For loop wil continue running from the start till finish of the data set
    for n in range (step,data_length+1,step):

        #Variable prices will be based on column 'Close/Last' in reverse order
        prices= df['Close/Last'].iloc[:n]

        #This will calulcate the daily change in stock price and will print out
        daily_changes = prices.diff().dropna().values
    

        #Calculate the total time taken to sort the daily changes of the stock price
        start_time=time.perf_counter()
        np.sort(daily_changes)
        end_time=time.perf_counter()
        elapsed = end_time - start_time

        #The list will be appended of the sorted n values and the time taken for each value to be sorted into its position
        n_values.append(n)
        time_values.append(elapsed)

        print(f"Sorted {n} daily changes in {elapsed:.6f} seconds.")
    
    #This will create a numpy array fro the number of data points, time taken to sort the data and a logarthmic function is created
    n_arr=np.array(n_values)
    time_arr = np.array(time_values)
    nlogn=n_arr * np.log2(n_arr)

    #A plot is created of the time taken against the number of data points with suitable x and y labels, legend and title
    plt.figure(figsize=(10,5))
    plt.plot(n_arr, time_arr, label = 'Time vs n', marker='o')
    plt.plot(n_arr,nlogn/max(nlogn)*max(time_arr),label='Scaled n log n', linestyle='--')
    plt.xlabel('Input size n (days)')
    plt.ylabel('Time to sort (seconds)')
    plt.title('Sorting Time of Daily Price Changes vs Input Size')
    plt.legend()
    plt.grid(True)
    plt.savefig(os.path.join(save_dir,"Daily_price_change.png"))
    plt.show()

    return np.array(n_values),np.array(time_values)

#This will read the stock price dataframe and convert any datatypes to the datetime. It will also clean the data and remove the dollar sign
palantir_df=pd.read_csv('Palantir/HistoricalData.csv')
palantir_df['Date']=pd.to_datetime(palantir_df['Date'])
palantir_df=palantir_df.sort_values('Date')
palantir_df['Close/Last'] = palantir_df['Close/Last'].str.replace('$','',regex=False).astype(float)

calculate_daily_changes(palantir_df)
    