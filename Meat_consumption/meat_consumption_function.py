import pandas as pd
import matplotlib.pyplot as plt

def plot_meat_vs_population():
    # Filenames are in the same folder as this script, so just use filenames directly
    meat_csv_path = 'Meat_consumption/global-meat-projections-to-2050.csv'
    pop_csv_path = 'Meat_consumption/population-with-un-projections.csv'

    # Load data
    meat_df = pd.read_csv(meat_csv_path)
    pop_df = pd.read_csv(pop_csv_path)

    pop_df.rename(columns={'Population - Sex: all - Age: all - Variant: estimates': 'Population in billions'}, inplace=True)
    pop_df['Population in billions'] = pd.to_numeric(pop_df['Population in billions'], errors='coerce') / 1_000_000_000

    # Filter for World, years 1990-2013 in meat data
    meat_df_filtered = meat_df[(meat_df['Entity'] == 'World') & (meat_df['Year'] >= 1961) & (meat_df['Year'] <= 1965)]

    # Calculate total meat consumption by summing key meat types
    meat_df_filtered['Total Meat'] = meat_df_filtered[['Beef and Buffalo', 'Pigmeat', 'Sheep and goat', 'Poultry']].sum(axis=1)

    # Filter population data similarly
    pop_df_filtered = pop_df[(pop_df['Entity'] == 'World') &  (pop_df['Year'] >= 1961) &  (pop_df['Year'] <= 1965)]

    # Merge dataframes on Year
    merged_df = pd.merge(meat_df_filtered, pop_df_filtered[['Year', 'Population in billions']], on='Year')

    # Plotting
    fig, ax1 = plt.subplots(figsize=(10,6))

    # Left y-axis for meat consumption (converted to million tons for readability)
    ax1.plot(merged_df['Year'], merged_df['Total Meat'] / 1e6, 'b-', label='Total Meat (million tons)')
    ax1.set_xlabel('Year')
    ax1.set_ylabel('Meat Consumption (million tons)', color='b')
    ax1.tick_params(axis='y', labelcolor='b')

    # Right y-axis for population (converted to billions)
    ax2 = ax1.twinx()
    ax2.plot(merged_df['Year'], merged_df['Population in billions'] , 'r-', label='Population (billions)')
    ax2.set_ylabel('Population (billions)', color='r')
    ax2.tick_params(axis='y', labelcolor='r')

    plt.title('Global Meat Consumption vs Population (1990-2013)')
    fig.tight_layout()
    plt.show()

plot_meat_vs_population()