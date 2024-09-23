from utils import load_data

# Load data
df = load_data('data/social-media.csv')

def main():
    # Check for missing and duplicate data
    print(df.isnull().sum())
    print(df.duplicated().sum())
