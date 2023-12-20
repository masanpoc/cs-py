# It is common for students in large programs to develop their
# own "shorthand" for referring to classes. Data Structures and
# Algorithms, CS1332 at Georgia Tech, is commonly referred to
# as "DS&A". Big Data for Healthcare is commonly referred to
# as "BD4H". Human-Computer Interaction is commonly referred to
# as "HCI".
#
# Let's pretend for a moment that these shorthands all follow
# a set of formal rules. The rules are:
#
# - The first letter of each capitalized word is included in the
#   abbreviated shorthand. Capitalized words may appear after
#   spaces or hyphens.
# - If the word 'for' appears in the course title, it is replaced
#   by the numeral '4'.
# - If the word 'and' appearsin the course title, it is replaced
#   by the character '&'.
# - The first letter of any non-capitalized word except for 'for'
#   and 'and' is omitted from the abbreviated shorthand.
#
# Write a function called class_shorthand. class_shorthand should
# take as input a string representing a class name. It should return
# the abbreviated shorthand according to the rules above.
#
# For example:
#
# class_shorthand("Advanced Operating Systems") -> "AOS"
# class_shorthand("Data Structures and Algorithms") -> "DS&A"
# class_shorthand("Big Data for Healthcare") -> "BD4H"
# class_shorthand("Introduction to Information Security") -> "IIS"
# class_shorthand("Human-Computer Interaction") -> "HCI"
# class_shorthand("Introduction to Cyber-Physical Systems Security") -> ICPSS
#
# You may assume that only letters, spaces, and hyphens appear in
# the course names. You may assume every course name will have at
# least two capitalized words.


# Write your function below!
def class_shorthand(input_str):
    input_str = input_str.split()
    shorthand = ""
    for word in input_str:
        if word == "for":
            shorthand += "4"
        elif word == "and":
            shorthand += "&"
        elif "-" in word and word[0].isupper():
            word = word.split("-")
            shorthand += word[0][0] + word[1][0]
        elif word[0].isupper():
            shorthand += word[0]
    return shorthand


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print:
# AOS
# DS&A
# BD4H
# IIS
# HCI
# ICPSS
print(class_shorthand("Advanced Operating Systems"))
print(class_shorthand("Data Structures and Algorithms"))
print(class_shorthand("Big Data for Healthcare"))
print(class_shorthand("Introduction to Information Security"))
print(class_shorthand("Human-Computer Interaction"))
print(class_shorthand("Introduction to Cyber-Physical Systems Security"))
