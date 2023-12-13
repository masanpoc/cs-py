minimum = 2
maximum = 5


# Print the result of multiplying every number from minimum to
# maximum, including both minimum and maximum.
#
# For example, if minimum = 2 and maximum = 5, you would print
# 120: 2 * 3 * 4 * 5 = 120.
#
# You may assume minimum will always be less than
# maximum.


# Add your code here!
i = minimum
result = 1

while i < (maximum + 1):
    result *= i
    i += 1

print(result)
