# The math we typically do is in base 10: adding 10 to one digit
# increments the next digit. Thus, the smallest (furthest right)
# number is the ones digit, the next smallest is the tens digit,
# the next smallest is the hundreds digit, etc. A 5 in the ones
# slot adds 5 to the total; a 5 in the tens slot adds 50 (5 * 10)
# to the total; a 5 in the hundreds slot adds 500 to the total
# (5 * 100), etc.
#
# Octal is a way of representing a different base, base 8.
# The digits 0 through 7 represent the normal numbers; however,
# there is no 8 or 9. Instead,
#
# 8 is represented as 10 in octal. (1 in the 8s place, 0 in the 1s place).
#
# 9 is represented as 11 in octal (1 in the 8s place, 1 in the 1s place).
#
# Like base 10, octal has digit places: the ones digit, the
# 8s digit, the 64s digit, and the 512s digit. A 5 in the ones
# spot adds 5 to the total; in the 8s spot it adds 40 to the
# total (5 * 8), in the 64s spot it adds 320 (5 * 64), and in
# the 512s spot it adds 2560 (5 * 512). In 4 digits, octal can
# represent base 10 numbers up to 4,095 (8^4 - 1).
#
# Write a function called octal_to_decimal. octal_to_decimal
# will take one parameter, a string. You may assume the string
# will always have exactly 4 characters, and that all the
# characters will be a numeral from 0 to 7. Return the result
# of converting this octal number to a standard base-10 number.
#
# For example:
#
# octal_to_decimal("1111") -> 585
# octal_to_decimal("0001") -> 1
# octal_to_decimal("5555") -> 2925
# octal_to_decimal("7777") -> 4095


# Write your function here!
def octal_to_decimal(a_str):
    result = 0
    for idx in range(len(a_str) - 1, -1, -1):
        result += int(a_str[idx]) * (8 ** (len(a_str) - idx - 1))
    return result


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print: 585, 1, 2925, 4095
print(octal_to_decimal("1111"))
print(octal_to_decimal("0001"))
print(octal_to_decimal("5555"))
print(octal_to_decimal("7777"))
