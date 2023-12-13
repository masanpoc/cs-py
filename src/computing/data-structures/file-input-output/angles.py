# Recall Coding Problem 4.3.9 (Advanced), the free body
# diagram problem. If you were unable to solve that, we've
# included the sample answer in the dropdown in the top left
# -- feel free to use that to write your answer to this
# problem.
#
# Revise your code from that problem to use a file instead of
# a list as its parameter. Name this new function
# find_net_force_from_file. The function should take one
# parameter, the name of a file. The function should return
# the net magnitude and direction, just as it did in the other
# problem.
#
# Each line of the file will have two numbers, both integers:
# the first number will be the magnitude, and the second
# number will be the angle (in degrees, from -180 to 180).
# There will be a space between them.
#
# HINT: You may have multiple functions in your code if you
# want!
#
# HINT 2: Try to write this such that you can reuse as much
# of your earlier code as possible. Remember, when loading
# from a file, any text you load is initially a string. You'll
# almost certainly need to use the split() method.

from math import sin, cos, tan, asin, acos, atan2, radians, degrees, sqrt


# Add your function here!
def find_net_force(input_tuples):
    horizontal = 0
    vertical = 0
    for force in input_tuples:
        horizontal += force[0] * cos(radians(force[1]))
        vertical += force[0] * sin(radians(force[1]))
    final_magnitude = sqrt(horizontal**2 + vertical**2)
    final_angle = degrees(atan2(vertical, horizontal))
    return (round(final_magnitude, 1), round(final_angle, 1))


def find_net_force_from_file(filename):
    try:
        input_file = open(filename, "r")
        forces = list()
        for line in input_file:
            force_values = line.split(" ")
            forces.append((int(force_values[0]), int(force_values[1])))
        input_file.close()
        return find_net_force(forces)
    except Exception as error:
        print(error)


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print: (87.0, 54.4)
print(find_net_force_from_file("a_few_angles.txt"))
