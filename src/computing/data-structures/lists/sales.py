# Write a function called find_max_sales. find_max_sales will
# have one parameter: a list of tuples. Each tuple in the
# list will have two items: a string and an integer. The
# string will represent the name of a movie, and the integer
# will represent that movie's total ticket sales (in millions
# of dollars).
#
# The function should return the movie from the list that
# had the most sales. Return only the movie name, not the
# full tuple.


# Write your function here!
def find_max_sales(tuples):
    max_movie = tuples[0][0]
    max_sales = tuples[0][1]
    for item in tuples:
        if item[1] > max_sales:
            max_movie = item[0]
            max_sales = item[1]
    return max_movie


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print: Rogue One
movie_list = [
    ("Finding Dory", 486),
    ("Captain America: Civil War", 408),
    ("Deadpool", 363),
    ("Zootopia", 341),
    ("Rogue One", 529),
    ("The Secret Life of Pets", 368),
    ("Batman v Superman", 330),
    ("Sing", 268),
    ("Suicide Squad", 325),
    ("The Jungle Book", 364),
]
print(find_max_sales(movie_list))
