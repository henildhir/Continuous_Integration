import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import os

save_dir="Life_Expectancy"
life_expectancy_pd=pd.read_csv("Life_Expectancy/life_expectancy.csv")
life_expectancy_pd.columns = [col.strip() for col in life_expectancy_pd.columns]

# Convert 'Year' column to numeric values (coerce errors)
life_expectancy_pd["Year"] = pd.to_numeric(life_expectancy_pd["Year"], errors="coerce")

# Define countries to filter
countries = ["United Kingdom", "India", "Malawi"]

colors = {"United Kingdom":"red","India":"blue","Malawi":"black"}

polynomial_order_labels = [f'Order {i}' for i in range(1,10)]

for country in countries:
    country_data = life_expectancy_pd[
        (life_expectancy_pd["Entity"] == country) &
        (life_expectancy_pd["Year"].between(1950, 2015))
    ].sort_values(by="Year")

    x_train = country_data["Year"].values
    y_train = country_data["Period life expectancy at birth"].values
    max_year = x_train.max()

    plt.figure(figsize=(10, 7))

    # Plot polynomial fits and save line objects for a common legend
    lines = []
    for degree in range(1, 10):
        coeffs = np.polyfit(x_train, y_train, degree)
        poly = np.poly1d(coeffs)

        x_forecast = np.arange(x_train.min(), max_year + 11)
        y_forecast = poly(x_forecast)

        # Plot each polynomial fit, capture line for legend
        (line,) = plt.plot(x_forecast, y_forecast, label=f"Order {degree}")
        lines.append(line)

    # Plot data points for the country
    plt.scatter(x_train, y_train, color=colors[country], label=f"{country} data", zorder=5)

    plt.title(f"Polynomial Fits and 10-Year Forecast for {country}")
    plt.xlabel("Year")
    plt.ylabel("Life expectancy in years")

    # Show just the polynomial order legend once
    plt.legend(handles=lines + [plt.Line2D([], [], marker='o', color=colors[country], linestyle='', label=f'{country} data')],
               fontsize='small', loc='best')

    plt.tight_layout()

    # Save figure under country name
    filename=(f"{country.replace(' ', '_')}_polynomial_forecast.png")
    plt.savefig(os.path.join(save_dir,filename))
    # Show plot in individual window
    plt.show()