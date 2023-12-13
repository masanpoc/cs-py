from datetime import date


def get_todays_date():
    today = date.today()
    return f"{today.year}/{today.month}/{today.day}"


print(get_todays_date())
