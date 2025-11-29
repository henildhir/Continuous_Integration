#This will import all necessary functions

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
from scipy.stats import linregress

#This variable will store the directory of where the graphs will be saved
save_dir="Linear_regression"

#This function will generate 100 different points and will create a linear regression graph
def generate_data_graph(m, b, n_points=100, noise_std=1.0, csv_filename='data.csv', plot_filename='plot.png'):
    x = np.linspace(0, 10, n_points)

    #This will create some noise around the points using standard deviation and will create a y=mx+c line graph
    noise = np.random.normal(0, noise_std, n_points)
    y = m * x + b + noise

    #This creates a dataframe with columns x and y and will save it automatically to the csv file when updated
    df = pd.DataFrame({'x': x, 'y': y})
    df.to_csv(csv_filename, index=False)

    #The linregress function will take in parameters and will create a linear regression graph using arguments x and y
    slope, intercept, r_value, p_value, std_err = linregress(x, y)


    #The graph will be created with a legend and labels and will be saved to a png file in the folder
    plt.figure()
    plt.scatter(x, y, label='Data')
    plt.plot(x, m * x + b, 'r--', label='Original line')
    plt.plot(x, slope * x + intercept, 'g-', label='Fitted line')
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Synthetic Data and Fitted Line')

    #The graph will be saved into the correct folder with the save_dir as the directory
    plt.savefig(os.path.join(save_dir,plot_filename))

    plt.close()
    return slope, intercept

#This function will create a graph and be outputted with a linear regression model with noise
slope, intercept = generate_data_graph(m=2.0, b=1.0, noise_std=0.5, csv_filename='data.csv', plot_filename='plot.png')
print(f'Fitted slope: {slope}, Fitted intercept: {intercept}')