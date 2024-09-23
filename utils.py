import pandas as pd
import matplotlib.pyplot as plt

# function to load data
def load_data(csv_path):
    return pd.read_csv(csv_path)
import matplotlib.pyplot as plt

# Histogram function without plt.show()
def plot_histogram(data, column, bins=10, xlabel='', ylabel='', title='', color='blue', figure_num=None):
    plt.figure(num=figure_num)
    plt.hist(data[column], bins=bins, color=color, edgecolor='black')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)

# Scatter plot function without plt.show()
def plot_scatter(x, y, xlabel='', ylabel='', title='', color='purple', figure_num=None):
    plt.figure(num=figure_num)
    plt.scatter(x, y, c=color)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)

# Scatter plot with correlation (also without plt.show())
def plot_scatter_with_correlation(x, y, xlabel='', ylabel='', title='', color='purple', figure_num=None):
    correlation = x.corr(y)
    plt.figure(num=figure_num)
    plt.scatter(x, y, c=color)
    plt.title(f'{title} (Correlación: {correlation:.2f})')
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)


# Function to create bar graphs without plt.show()
def plot_bar(x, y, xlabel='', ylabel='', title='', color='blue', xticks_rotation=0, figure_num=None):
    """Creates a bar chart with the provided data and labels."""
    plt.figure(num=figure_num)  # Create a new figure for each plot
    plt.bar(x, y, color=color)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.title(title)
    plt.xticks(rotation=xticks_rotation)
    # plt.show() is removed to allow multiple plots to be shown together

# Function to calculate correlation by group
def group_correlation(df, group_col, x_col, y_col):
    """Calculates the correlation between two columns within each group of a DataFrame."""
    correlation_results = {}
    for group, group_df in df.groupby(group_col):
        correlation = group_df[x_col].corr(group_df[y_col])
        correlation_results[group] = correlation
    return pd.DataFrame.from_dict(correlation_results, orient='index', columns=['Correlation']).dropna()


