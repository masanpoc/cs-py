original_number = 5

# Write some code that will triple original_number in three ways,
# in this order:
#
# - First, triple the number by cubing it (raising it to the
#   3rd power)
# - Second, triple the number by duplicating it 3 times.
# - Third, triple the number by multiplying it by 3 again.
#
# For example, original_number 5 would first be cubed into
# 125 (5^3 = 125), then it would be tripled to 125125125
# (duplicating 125 three times), and then it would be tripled
# to 375375375 (125125125 * 3 = 375375375).
#
# Print out the number after you've tripled it all three times.


# Add your code here!
original_number **= 3
original_number = int(str(original_number) * 3)
original_number *= 3
print(original_number)
