# Write a function called recent_median. recent_median should
# take as input one parameter, a list of integers. recent_median
# should return the median of the last five numbers in the list.
#
# The median is the middle number when the numbers are sorted.
# For example:
#
# recent_median([6, 1, 2, 9, 8, 3, 4, 5, 7]) -> 5
#
# The last five numbers in the list are: 8, 3, 4, 5, 7. The median
# of these numbers (that is, the middle number when sorted) is 5.


# Write your function here!
def recent_median(num_data):
    num_data = num_data[-5:]
    num_data.sort()
    return num_data[len(num_data) // 2]


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print: 5, 35, 29, each on its own line
print(recent_median([6, 1, 2, 9, 8, 3, 4, 5, 7]))
print(recent_median([15, 83, 25, 63, 11, 96, 35, 76, 12, 13]))
print(recent_median([9, 21, 41, 24, 96, 66, 0, 54, 29, 29, 77, 5]))
