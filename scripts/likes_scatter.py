from utils import load_data, plot_scatter_with_correlation

def main():
    # Load data
    df = load_data('data/social-media.csv')

    # Get the required columns
    likes = df['TotalLikes']
    usage = df['UsageDuration']

    # Graph the relationship between Duration of Use and Total Likes
    plot_scatter_with_correlation(usage, likes, xlabel='Duration of use (hours)', ylabel='Total Likes', title='Correlation between Duration of Use and Total Likes', figure_num=7)
