# Recall in Worked Example 5.2.5 that we showed you the code
# for two versions of binary_search: one using recursion, one
# using loops. For this problem, use the recursive one.
#
# In this problem, we want to implement a new version of
# binary_search, called binary_search_year. binary_search_year
# will take in two parameters: a list of instances of Date,
# and a year as an integer. It will return True if any date
# in the list occurred within that year, False if not.
#
# For example, imagine if listOfDates had three instances of
# date: one for January 1st 2016, one for January 1st 2017,
# and one for January 1st 2018. Then:
#
#  binary_search_year(listOfDates, 2016) -> True
#  binary_search_year(listOfDates, 2015) -> False
#
# You should not assume that the list is pre-sorted, but you
# should know that the sort() method works on lists of dates.
#
# Instances of the Date class have three attributes: year,
# month, and day. You can access them directly, you don't
# have to use getters (e.g. myDate.month will access the
# month of myDate).
#
# You may copy the code from Worked Example 5.2.5 and modify
# it instead of starting from scratch. You must implement
# binary_search_year recursively.
#
# Don't move this line:
from datetime import date


# Write your code here!
def binary_search_year(searchList, searchTerm):
    # First, the list must be sorted.
    searchList.sort()

    # With each recursive call to binary_search, the size
    # of the list will be cut in half, rounding down. If
    # the search term is not found, then eventually an
    # empty list will be passed into binary_search. So,
    # if searchList is empty, we know that the search
    # term was not found, and we can return False. This
    # is the base case for the recursive binary_search.

    if len(searchList) == 0:
        return False

    # If there are still items in the list, then we want
    # to find if searchTerm is greater than, less than,
    # or equal to the middle term in the list. For that,
    # we need the index of the middle term.

    middle = len(searchList) // 2

    # First, the easy case: if it's the middle term, we
    # found it! Return True.
    if searchList[middle].year == searchTerm:
        return True

    # If the search term is less than the middle term,
    # then repeat the search on the left half of the
    # list.
    elif searchTerm < searchList[middle].year:
        return binary_search_year(searchList[:middle], searchTerm)

    # If the search term is greater than the middle
    # term, then repeat the search on the right half
    # of the list.
    else:
        return binary_search_year(searchList[middle + 1 :], searchTerm)

    # As long as there are items to be searched, binary_search_year
    # will keep getting called on smaller and smaller lists,
    # until eventually the item is found or the list of possible
    # places it could be found is empty.


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print: True, then False
listOfDates = [
    date(2016, 11, 26),
    date(2014, 11, 29),
    date(2008, 11, 29),
    date(2000, 11, 25),
    date(1999, 11, 27),
    date(1998, 11, 28),
    date(1990, 12, 1),
    date(1989, 12, 2),
    date(1985, 11, 30),
]

print(binary_search_year(listOfDates, 2016))
print(binary_search_year(listOfDates, 2007))
