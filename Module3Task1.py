from datetime import datetime

def get_days_from_today(date):
    # Convertion of the string date to datetime object
    given_date = datetime.strptime(date, "%Y-%m-%d").date()

    # Get today's date
    now = datetime.today().date()

    # Calculate the difference in days
    delta = now - given_date

    # Return the number of days as an integer
    return delta.days
# test -> returned 988 days as for 23.06.2024
date = "2021-10-09"
days_difference = get_days_from_today(date)
print(f"Days difference from {date} to today: {days_difference} days")