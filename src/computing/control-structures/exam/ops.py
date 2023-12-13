a = 4
b = 3

# Attempt to perform the four arithmetic operations (a plus b,
# a minus b, a times b, a divided by b, in that order) between
# a and b and print the result of each on its own line.
#
# If one of the operations cannot work for ANY reason, print
# Error! for that operation instead. You should still print the
# results of the other operations, though.
#
# For any numeric results, round the result to 2 decimal
# places using round(the_num, 2). Note that if the_num is an
# integer, this won't change the number; that's okay! However,
# note that trying to round a string will also cause an error;
# in that case, you would still print the string, not "Error!"
# Only print "Error!" if the error arises from the arithmetic
# operation, not the rounding.
#
# Remember, arithmetic operators still work on some non-numeric
# values: for example, we can multiply a string by an integer,
# add two strings together, or use booleans in mathematical
# expressions.
#
# For example, for the initial values of a and b above, you
# should print:
# Error!    -> we can't add an integer and a string!
# Error!    -> we can't subtract a string from an integer!
# ScoreScoreScoreScore   -> we can multiply a string by an int!
# Error!    -> we can't divide an integer by a string!
#
# If a and b were changed to 4 and 3, you would print:
# 7
# 1
# 12
# 1.33


# Add your code here!
for op in ["+", "-", "*", "/"]:
    try:
        if op == "+":
            the_num = a + b
        elif op == "-":
            the_num = a - b
        elif op == "*":
            the_num = a * b
        else:
            the_num = a / b

        if type(the_num) is str:
            print(the_num)
        else:
            print(round(the_num, 2))
    except Exception as error:
        print("Error!")
