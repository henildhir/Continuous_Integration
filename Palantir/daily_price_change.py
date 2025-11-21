import time
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

#Function to calculate the daily changes of stock price of Palantir
def calculate_daily_changes(df, max_days=365, step=7):
    # palantir_df=pd.read_csv('Palantir/HistoricalData.csv')
    # palantir_df['Date']=pd.to_datetime(palantir_df['Date'])
    # palantir_df=palantir_df.sort_values('Date')
    # palantir_df['Close/Last'] = palantir_df['Close/Last'].str.replace('$','',regex=False).astype(float)

    n_values = []
    time_values = []

    data_length = min(len(df),max_days)

    for n in range (step,data_length+1,step):
        prices= df['Close/Last'].iloc[:n]
        daily_changes = prices.diff().dropna().values
        print(daily_changes)

        start_time=time.perf_counter()
        np.sort(daily_changes)
        end_time=time.perf_counter()

        elapsed = end_time - start_time
        n_values.append(n)
        time_values.append(elapsed)
        print(f"Sorted {n} daily changes in {elapsed:.6f} seconds.")
    
    n_arr=np.array(n_values)
    time_arr = np.array(time_values)
    nlogn=n_arr * np.log2(n_arr)

    plt.figure(figsize=(10,5))
    plt.plot(n_arr, time_arr, label = 'Time vs n', marker='o')
    plt.plot(n_arr,nlogn/max(nlogn)*max(time_arr),label='Scaled n log n', linestyle='--')
    plt.xlabel('Input size n (days)')
    plt.ylabel('Time to sort (seconds)')
    plt.title('Sorting Time of Daily Price Changes vs Input Sizee')
    plt.legend()
    plt.grid(True)
    plt.show()

    return np.array(n_values),np.array(time_values)

palantir_df=pd.read_csv('Palantir/HistoricalData.csv')
palantir_df['Date']=pd.to_datetime(palantir_df['Date'])
palantir_df=palantir_df.sort_values('Date')
palantir_df['Close/Last'] = palantir_df['Close/Last'].str.replace('$','',regex=False).astype(float)

calculate_daily_changes(palantir_df)
    
#print(palantir_df)
# calculate_daily_changes(palantir_df)