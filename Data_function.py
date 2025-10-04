import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy.stats import linregress

def generate_data_graph(m, b, n_points=100, noise_std=1.0, csv_filename='data.csv', plot_filename='plot.png'):
    x = np.linspace(0, 10, n_points)
    noise = np.random.normal(0, noise_std, n_points)
    y = m * x + b + noise
    df = pd.DataFrame({'x': x, 'y': y})
    df.to_csv(csv_filename, index=False)
    slope, intercept, r_value, p_value, std_err = linregress(x, y)
    plt.figure()
    plt.scatter(x, y, label='Noisy data')
    plt.plot(x, m * x + b, 'r--', label='Original line')
    plt.plot(x, slope * x + intercept, 'g-', label='Fitted line')
    plt.legend()
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title('Synthetic Data and Fitted Line')
    plt.savefig(plot_filename)
    plt.close()
    return slope, intercept