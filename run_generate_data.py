from functions.Data_function import generate_data_graph

slope, intercept = generate_data_graph(m=2.0, b=1.0, noise_std=0.5, csv_filename='data.csv', plot_filename='plot.png')
print(f'Fitted slope: {slope}, Fitted intercept: {intercept}')