mystery_value_1 = 6
mystery_value_2 = 3

# You may modify the lines of code above, but don't move them!
# When you Submit your code, we'll change these lines to
# assign different values to the variables.
#
# Print a sentence describing the values you get when you add,
# subtract, multiply, and divide the numbers above. The
# sentence should look like this:
#
# The sum is 9, the difference is 3, the product is 18, and the
# quotient is 2.0.
#
# Make sure to include all commas, spaces, and periods exactly
# as shown -- the only thing that should change based on the
# values of the variables is the numbers.


# Add your code here!
sum_num = mystery_value_1 + mystery_value_2
diff_num = mystery_value_1 - mystery_value_2
product_num = mystery_value_1 * mystery_value_2
division_num = mystery_value_1 / mystery_value_2

output = "The sum is {0}, the difference is {1}, the product is {2}, and the quotient is {3}.".format(
    sum_num, diff_num, product_num, division_num
)
print(output)
print("or also")
print(
    f"The sum is {sum_num}, the difference is {diff_num}, the product is {product_num}, and the quotient is {division_num}."
)
