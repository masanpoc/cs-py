# Write a function called "in_parentheses" that accepts a
# single argument, a string representing a sentence that
# contains some words in parentheses. Your function should
# return the contents of the parentheses.
#
# For example:
#
# in_parentheses("This is a sentence (words!)") -> "words!"
#
# If no text appears in parentheses, return an empty string.
# Note that there are several edge cases introduced by this:
# all of the following function calls would return an empty
# string:
#
# in_parentheses("No parentheses")
# in_parentheses("Open ( only")
# in_parentheses("Closed ) only")
# in_parentheses("Closed ) before ( open")
#
# You may assume, however, that there will not be multiple
# open or closed parentheses.


# Write your function here!
def in_parentheses(a_string):
    # count & compare opening + closing parentheses
    closing_parentheses = a_string.count(")")
    opening_parentheses = a_string.count("(")
    # if different or none
    if closing_parentheses != opening_parentheses or opening_parentheses == 0:
        return ""
    # check if closed before opened
    start_idx = a_string.find("(")
    end_idx = a_string.find(")")
    if end_idx < start_idx:
        return ""
    # replace
    return a_string[start_idx + 1 : end_idx]


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print (including the blank lines):
# words!
#
# as he is doing right now
#
#
#!

print(in_parentheses("This is a sentence (words!)."))
print(in_parentheses("No parentheses here!"))
print(
    in_parentheses(
        "David tends to use parentheses a lot (as he is doing right now). It tends to be quite annoying."
    )
)
print(in_parentheses("Open ( only"))
print(in_parentheses("Closed ) only"))
print(in_parentheses("Closed ) before ( open"))
print(in_parentheses("That's a lot of test cases(!)"))
