principal = 5000
rate = 0.05
time = 5
goal = 7000


#   amount = principal * e ^ (rate * time)
#
# We want to see if the investment given by
# these values will exceed the goal. If it will, we want to
# print this message:
#
#  "You'll exceed your goal by [extra money]"
#
# If it will not, we want to print this message:
#
#  "You'll fall short of your goal by [needed money]"
#
# If the investor will meet their goal, [extra money] should
# be the final amount minus the goal. If the investor will
# not meet their goal, [needed money] will be the goal minus
# the final amount.
#
# To make the output more legible, though, we want to round
# the difference to two decimal places. If the difference is
# contained in a variable called 'difference', then we can
# do this to round it: rounded_diff = round(difference, 2)
#
# Working with new and unfamiliar functions or abilities is
# part of learning to code, so use this function in your
# answer!

from math import e

# Remember, you can access e with math.e.
amount = principal * (e ** (rate * time))
rounded_diff = round(amount - goal, 2)

if rounded_diff > 0:
    print(f"You'll exceed your goal by {rounded_diff}")
else:
    print(f"You'll fall short of your goal by {abs(rounded_diff)}")
