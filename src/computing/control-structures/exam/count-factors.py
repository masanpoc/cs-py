# Write a function called count_factors. count_factors should
# take as input one integer. It should return a count of the
# number of factors that number has. You should not include 1
# or the number itself among its factors.
#
# For example, count_factors(6) would return 2: 6 has two
# factors, 2 and 3.
#
# As a reminder, x is a factory of y if the remainder of
# dividing y by x is 0. In the case of count_factors(6), the
# answer is 2 because 6 % 2 = 0 and 6 % 3 = 0.


# Add your code here!
def count_factors(an_int):
    factors = 0
    for i in range(2, an_int):
        if an_int % i == 0:
            factors += 1
    return factors


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print: 2, 0, 2, 6, each on their own line.
print(count_factors(6))
print(count_factors(7))
print(count_factors(8))
print(count_factors(24))
