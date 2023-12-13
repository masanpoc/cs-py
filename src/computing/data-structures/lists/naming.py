# You've been sent a list of names. Unfortunately, the names
# come in two different formats:
#
# First Middle Last
# Last, First Middle
#
# You want the entire list to be the same. For this problem,
# we'll say you want the entire list to be Last, First Middle.
#
# Write a function called name_refixer. name_refixer should take
# as input the list of strings. You may assume that every string
# will match one of the two formats above: either First Middle Last
# or Last, First Middle.
#
# name_fixer should return a list of names all structured as
# Last, First Middle. If the name was already structured as
# Last, First Middle, it should remain unchanged. If it was
# structured as First Middle Last, then Last should be moved
# to the beginning and a comma should be added after it.
#
# The names should appear in the same order as the original list.
#
# For example:
#
# name_list = ["David Andrew Joyner", "Hart, Melissa Joan", "Cyrus, Billy Ray"]
# name_fixer(name_list) -> ["Joyner, David Andrew", "Hart, Melissa Joan", "Cyrus, Billy Ray"]


# Add your code here!
def name_refixer(name_list):
    for i in range(len(name_list)):
        if "," not in name_list[i]:
            name_list[i] = name_list[i].split()
            name_list[i] = f"{name_list[i][2]}, {name_list[i][0]} {name_list[i][1]}"
    return name_list


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print:
# ["Joyner, David Andrew", "Hart, Melissa Joan", "Cyrus, Billy Ray"]
name_list = ["David Andrew Joyner", "Hart, Melissa Joan", "Cyrus, Billy Ray"]
print(name_refixer(name_list))
