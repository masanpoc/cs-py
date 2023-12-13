current_day = 12
current_month = 10
current_year = 2020
exp_day = 11
exp_month = 10
exp_year = 2022

# Given the current date and expiration date held by the
# variables above, determine whether a food with the listed
# expiration date has expired. Print True if it has expired,
# False if it has not. A food is defined as expired if the
# current date is _after_ the expiration date, not equal to
# it.


# Add your code here!

is_expired = (current_year > exp_year) or (
    current_year == exp_year
    and (
        current_month > exp_month
        or (current_month == exp_month and current_day > exp_day)
    )
)

print(is_expired)
