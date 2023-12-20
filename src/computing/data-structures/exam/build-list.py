# Write a function called expand_to_list. expand_to_list should
# have two parameters, both integers. For thise description, we
# will refer to these integers as mid and n.
#
# expand_to_list should return a list, such that the middle
# number of the list is mid, and there are n numbers on either
# side in incremental ascending order.
#
# Here are a few examples:
#
# expand_to_list(5, 2) -> [3, 4, 5, 6, 7]
#
# 5 is the middle number, and there are 2 numbers before it and
# 2 numbers after it.
#
# expand_to_list(10, 4) -> [6, 7, 8, 9, 10, 11, 12, 13, 14]
#
# 10 is the middle number, and there are 4 numbers before it
# and 4 numbers after it.
#
# expand_to_list(0, 1) -> [-1, 0, 1]
#
# 0 is the middle number, and there is 1 number before it and
# 1 number after it.


# Write your function here!
def expand_to_list(mid, n):
    result = [mid]
    low_num = mid - 1
    big_num = mid + 1
    for i in range(n):
        result.insert(0, low_num)
        result.append(big_num)
        low_num -= 1
        big_num += 1
    return result


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print:
# [3, 4, 5, 6, 7]
# [6, 7, 8, 9, 10, 11, 12, 13, 14]
# [-1, 0, 1]
print(expand_to_list(5, 2))
print(expand_to_list(10, 4))
print(expand_to_list(0, 1))
