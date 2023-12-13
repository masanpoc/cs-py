lyrics = [
    "I wanna be your endgame",
    "I wanna be your first string",
    "I wanna be your A-Team",
    "I wanna be your endgame, endgame",
]
lines_of_sanity = 6

#
# Revise that code so that you always stop when lines_of_sanity
# is reached. If lines_of_sanity is 6, you would print 6 lines,
# no matter how many lines are in the list. If there are fewer
# than 6 lines in the list, then you'd repeat the list until
# the number of lines is reached.
#
# For example, with the values above, you'd print:
# I wanna be your endgame
# I wanna be your first string
# I wanna be your A-Team
# I wanna be your endgame, endgame
# I wanna be your endgame
# I wanna be your first string
# MAKE IT STOP
#
# That's 6 lines: the entire list once, then the first two lines
# again to reach 6. As before, print MAKE IT STOP when you're
# done.
#
# HINT: There are multiple ways to do this: some involve a small
# change to our earlier answer, others involve a more wholesale
# rewrite. If you're stuck on one, try to think of a totally
# different way!


# Add your code here! Using the initial inputs from above, this
# should print 7 lines: all 4 lines of the list, then the first
# two lines again, then MAKE IT STOP

while lines_of_sanity > 0:
    for line in lyrics:
        print(line)
        lines_of_sanity -= 1
        if lines_of_sanity == 0:
            break
print("MAKE IT STOP")
