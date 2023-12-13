mystery_int = 51

# Add some code below that will find and print the sum of
# every odd number between 0 and mystery_int. This time,
# exclude the bounds (e.g. if mystery_int was 51, add the odds
# from 1 to 49, but not 51).
#
# Hint: There are multiple ways to do this!


# Add your code here!
sum_odds = 0

for i in range(1, mystery_int, 2):
    sum_odds += i

print(sum_odds)
