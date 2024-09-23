from utils import load_data, group_correlation, plot_bar

def main():
    # Load data
    df = load_data('data/social-media.csv')

    # Count users by country
    country_counts = df['Country'].value_counts()

    # Graph the number of users by country
    plot_bar(country_counts.index, country_counts.values, xlabel='Country', ylabel='Number of Users', title='Number of users by country', xticks_rotation=45, figure_num=2)

    # Calculate correlation between Duration of Use and Likes by country
    correlation_df = group_correlation(df, 'Country', 'UsageDuration', 'TotalLikes')

    # Plot the correlation by country
    plot_bar(correlation_df.index, correlation_df['Correlation'], xlabel='Country', ylabel='Correlation', title='Correlation between Usage and Likes by Country', xticks_rotation=45, figure_num=3)
