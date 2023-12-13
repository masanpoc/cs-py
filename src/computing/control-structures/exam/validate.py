# A credit card transaction is defined, at a minimum, by
# the card number, CVV code, and expiration date of a
# credit card. The card provider (Visa, Mastercard,
# American Express, or Discover) can be inferred from
# the number, but we'll have it provided directly.
#
# Write a function called validate_card. validate_card
# should have four positional parameters and one keyword
# parameter. The parameters should be, in this order:
#
# - number: the card number, a 15- or 16-character
#   string.
# - cvv: the verification number, a 3- or 4-character
#   string.
# - expiration_month: an integer from 1 to 12 giving
#   the expiration month.
# - expiration_year: an integer from 22 to 28 giving
#   the expiration year.
# - provider: a string representing the card provider,
#   either "Visa", "MasterCard", "Discover", or
#   "American Express". provider should be a keyword
#   parameter with a default value of "Visa".
#
# You may assume that proper data types will be supplied
# (e.g. we'll never pass an integer for CVV, a string for
# expiration_year, a float for provider, etc.).
#
# Your code should return True if the card information
# represented by these five variables is valid, or False
# if not.
#
# Here are the details to validate about the card info:
# - The card numbers for Visa, MasterCard, and Discover
#   are 16 numbers long. For American Express, card
#   numbers are 15 numbers long.
# - The CVV for Visa, MasterCard, and Discover is 3
#   numbers long. For American Express, the CVV is
#   4 numbers long.
# - For all cards, the card number and CVV are all
#   numerals, no letters or punctuation marks.
# - All expiration months must be between 1 and 12.
# - All expiration years must be between 22 and 28.
# - All providers must be "Visa", "MasterCard",
#   "Discover", or "American Express".
#
# If a card breaks any of these rules, it is invalid,
# and you should return False. If a card follows all of
# these rules, it is valid, and you should return True.


# Write your function here!
def validate_card(number, cvv, expiration_month, expiration_year, provider="Visa"):
    if provider not in ["Visa", "MasterCard", "Discover", "American Express"]:
        return False

    if provider == "American Express":
        if (len(number) != 15) or (len(cvv) != 4):
            return False
    else:
        if (len(number) != 16) or (len(cvv) != 3):
            return False

    if expiration_month not in range(1, 13) or expiration_year not in range(22, 29):
        return False

    for char in number:
        if not char.isdigit():
            return False

    for char in cvv:
        if not char.isdigit():
            return False

    return True


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print the values shown in the comments

# True
print(validate_card("1234567890123456", "123", 1, 22))

# True
print(validate_card("1234567890123456", "123", 1, 22, provider="MasterCard"))

# False (American Express cards have 15 digits, not 16)
print(validate_card("1234567890123456", "123", 1, 22, provider="American Express"))

# False (Visa cards have 16 digits, not 15)
print(validate_card("123456789012345", "1234", 1, 22))

# True
print(validate_card("123456789012345", "1234", 1, 22, provider="American Express"))

# False (no card numbers have only 12 digits)
print(validate_card("123456788012", "123", 1, 22))

# False (no cards have 5-digit CVVs)
print(validate_card("1234567890123456", "15062", 1, 22))

# False (no cards have an expiration month of 13)
print(validate_card("1234567890123456", "123", 13, 22))

# False (no cards have an expiration year of 18)
print(validate_card("1234567890123456", "123", 1, 18))

# False (Diner's Club is not a valid provider)
print(validate_card("1234567890123456", "123", 1, 22, provider="Diner's Club"))

# False (no cards have the letter A in the number)
print(validate_card("123456789A123456", "123", 1, 22))

# False (no cards have letters in the CVV)
print(validate_card("1234567890123456", "ABC", 1, 22))
