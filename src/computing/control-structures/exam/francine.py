# Write a function that will calculate the Francine index of
# a number. The Francine Index is a thing I made up for this
# problem, and it is defined as follows:
#
# Start with the number.

# If the number is a multiple of 3 (e.g.
# 3, 6, 9),
# divide it by 3
#
# (use floor division to keep it as
# an integer).

# If the number is +1 than a multiple of
# three (e.g. 4, 7, 10),
# add 2 to the number.
#
# If the number is +2 than a multiple of three (e.g. 5, 8, 11),
# double the number.
#
# If you continue repeating this sequence, the number will
# eventually reach either 1 or 2, at which point the sequence
# would repeat either 2-4-6 or 1-3 forever.
#
# For example, imagine we started with the number 50:
# 50 is two more than the nearest multiple of 3, so 50 * 2 = 100
# 100 is one more than the nearest multiple of 3, so 100 + 2 = 102
# 102 is a multiple of 3, so 102 // 3 = 34
# 34 is one more than the nearest multiple of 3, so 34 + 2 = 36
# 36 is a multiple of 3, so 36 // 3 = 12
# 12 is a multiple of 3, so 12 // 3 = 4
# 4 is one more the the nearest multiple of 3, so 4 + 2 = 6
# 6 is a multiple of 3, so 6 // 3 = 2
#
# Starting with 50, this sequence converges on 2 in 8 iterations:
# 50 to 100, 100 to 102, 102 to 34, 34 to 36, 36 to 12, 12 to 4,
# 4 to 6, and 6 to 2.
#
# Implement a function called francine. francine should take as
# input an integer, and return the integer's Francine Index;
# that is, the number of iterations it takes for the
# number to reach either 1 or 2 the first time following those rules.
# For example, francine(50) would return 8 because it took 8
# iterations to converge on 2.


# Add your code here!
def francine(an_int):
    i = an_int
    count = 0
    while i not in [1, 2]:
        if i % 3 == 0:
            i //= 3
        elif i % 3 == 1:
            i += 2
        elif i % 3 == 2:
            i *= 2
        count += 1
    return count


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print: 8, 6, and 10, each on their own lines.
print(francine(50))
print(francine(15))
print(francine(124))
