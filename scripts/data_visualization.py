from utils import load_data

# Load data
df = load_data('data/social-media.csv')

# Preview the df
def main():
    print(df.head())
    print(df.tail())
    print(df.info())
