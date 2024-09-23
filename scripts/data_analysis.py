from utils import load_data

def main():
    # Load data
    df = load_data('data/social-media.csv')

    # Total users
    users = df['UserId'].nunique()
    print(f"Total Users: {users}")

    # Users with > 5 hours of usage
    usage = len(df.query('UsageDuration > 5 '))
    print(f"Userss with > 5 hours of usage: {usage}")

    # Percetage of users with > 5 hours of usage
    percentage = (usage / users) * 100
    print(f"Percetage of users with > 5 hours of usage: {percentage}%")

    # Correlation between age and duration of use
    corr = df['Age'].corr(df['UsageDuration'])
    print(f"Correlation between age and duration of use: {corr}")
