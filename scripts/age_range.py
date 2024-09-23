from utils import load_data, plot_bar
import pandas as pd

def main():
    # Load data
    df = load_data('data/social-media.csv')

    # Create age groups
    bins = [18, 24, 34, 44, 54, 64]
    labels = ['18-24', '25-34', '35-44', '45-54', '55-64']
    df['AgeGroup'] = pd.cut(df['Age'], bins=bins, labels=labels)

    # group by age and calculate medians
    grouped = df.groupby('AgeGroup')
    median_usage = grouped['UsageDuration'].median()
    median_likes = grouped['TotalLikes'].median()

    # Plot bars for medians of usage and likes
    plot_bar(range(len(median_usage)), median_usage, xlabel='Age groups', ylabel='Median usage', title='Median usage by group age', figure_num=5)
    plot_bar(range(len(median_likes)), median_likes, xlabel='Age groups', ylabel='Median likes', title='Median likes by group age', figure_num=6)

    # Filter and calculate median likes for the 18-24 age group
    median_likes_18_24 = df[df['AgeGroup'] == '18-24']['TotalLikes'].median()
    print(f"Medi {median_likes_18_24}")
