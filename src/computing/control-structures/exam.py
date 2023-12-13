grade = 82
curve = 8


# Prof. Burdell then wants to send one of the following
# messages, depending on the student's final grade:
#
# - If the total grade 90 to 100, the message would state:
#   "Congratulations! Your final grade is [their grade], an A."
# - If the total grade is 80 to 89, the message would state:
#   "Good job! Your final grade is [their grade], a B."
# - If the total grade is 70 to 79, the message would state:
#   "Not bad! Your final grade is [their grade], a C."
# - If the total grade is 60 to 69, the message would state:
#   "You passed! Your final grade is [their grade], a D."
# - If the total grade is under 60, the message would state:
#   "It's just one grade. Your final grade is [their grade], an F."
#
# [their grade] should be the result of adding grade and curve,
# but should not be greater than 100.


# Add your code here!
total = grade + curve

if total > 100:
    total = 100

if total < 60:
    print(f"It's just one grade. Your final grade is {total}, an F.")
elif total <= 69:
    print(f"You passed! Your final grade is {total}, a D.")
elif total <= 79:
    print(f"Not bad! Your final grade is {total}, a C.")
elif total <= 89:
    print(f"Good job! Your final grade is {total}, a B.")
else:
    print(f"Congratulations! Your final grade is {total}, an A.")
