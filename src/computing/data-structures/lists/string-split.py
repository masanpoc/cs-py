# Write a function called string_splitter that replicates the
# function of the string type's split() method, assuming that
# we're splitting at spaces. string_splitter should take as
# input a string, and return as output a list of the
# individual words from the string, assuming that words were
# divided by spaces. The spaces themselves should not be in
# the list that your function returns.
#
# You may assume that there will never be more than one space
# in a row, and that the string will neither start nor end
# with a space. However, you should not assume there will
# always be a space.
#
# You may not use Python's built-in split() method.
#
# For example:
#
#  string_splitter("Hello world") -> ['Hello', 'world']


# Write your function here!
def string_splitter(a_string):
    result = list()
    word = ""
    if " " not in a_string:
        return [a_string]

    for char in a_string:
        if char == " ":
            result.append(word)
            word = ""
        else:
            word += char
    result.append(word)
    return result


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print: ['Hello', 'world']
print(string_splitter("Hello world"))
