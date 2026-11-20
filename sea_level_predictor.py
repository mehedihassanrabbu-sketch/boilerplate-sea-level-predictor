import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy.stats import linregress


def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')

    # Create scatter plot
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.scatter(df['Year'], df['CSIRO Adjusted Sea Level'])

    # First line of best fit: all data up to 2050
    res_all = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
    years_all = np.arange(df['Year'].min(), 2051)
    line_all = res_all.intercept + res_all.slope * years_all
    ax.plot(years_all, line_all, 'r', label='Fit: All Years')

    # Second line of best fit: data from year 2000 onward up to 2050
    recent = df[df['Year'] >= 2000]
    res_recent = linregress(recent['Year'], recent['CSIRO Adjusted Sea Level'])
    years_recent = np.arange(2000, 2051)
    line_recent = res_recent.intercept + res_recent.slope * years_recent
    ax.plot(years_recent, line_recent, 'g', label='Fit: 2000+')

    # Add labels and title
    ax.set_xlabel('Year')
    ax.set_ylabel('Sea Level (inches)')
    ax.set_title('Rise in Sea Level')
    ax.legend()

    # Save plot and return for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()