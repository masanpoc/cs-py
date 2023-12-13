# Every character in Python has what is called an ordinal
# number. The ordinal number is an integer Python uses to
# store what each character should be. For example, the
# ordinal number for a lower-case a is 97. The ordinal number
# for an upper-case A is 65.
#
# To get the ordinal number for any character, you can use
# the ord() function:
#
# the_ord_for_a = ord("a")
# the_ord_for_B = ord("B")
#
# ...and so on. ord() must take a string with only one
# character, and it will always return an integer.
#
# Write a function called string_to_ordinals. This function
# should take as input a single parameter, a string.
#
# string_to_ordinals should return a new string made of all
# the ordinal numbers for the characters in the original
# string.
#
# For example, the ordinals for "A", "B", and "C" are 65,
# 66, and 67, respectively. So, string_to_ordinals("ABC")
# would return "656667". Or, the ordinals for "x", "y", and
# "z" are 120, 121, and 122, respectively. So,
# string_to_ordinals("xyz") would return "120121122".


# Write your function here!
def string_to_ordinals(a_str):
    result = ""
    for char in a_str:
        result += str(ord(char))
    return result


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print:
# 656667
# 120121122
# 678349514849
# 633363336333
# 3232323232
print(string_to_ordinals("ABC"))
print(string_to_ordinals("xyz"))
print(string_to_ordinals("CS1301"))
print(string_to_ordinals("?!?!?!"))
print(string_to_ordinals("     "))
