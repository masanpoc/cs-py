story = "A"
text = "B"
role = "C"
director = "D"
cast = "F"

# assign the script a grade in each of five categories: Story, Text, Role, Director,
# and Cast.
#
# into a total score for the
# script, according to the following chart:
#
#            A   B   C   D   F
# Story     +6  +5  +4  +2  +0
# Text      +5  +4  +3  +1  +0
# Role      +4  +3  +2  +1  +0
# Director  +3  +2  +1  +0  +0
# Cast/Misc +2  +1  +0  +0  +0
#
# For example: an A story, B text, C role, D directory, and
# F cast would get a score of 12: +6 for the story, +4 for the
# text, +2 for the role, +0 for the director, and +0 for the
# cast.
#
# 20: Perfect score
# 17 to 19: Must do
# 14 to 16: Seriously consider
# 12 to 13: On the bubble
# 11 or below: Pass
#
# print the category
# he would assign to that script. For example, for the values
# above, this program would print:
#
# 12
# On the bubble
#
score = 0

if story == "A":
    score += 6
elif story == "B":
    score += 5
elif story == "C":
    score += 4
elif story == "D":
    score += 2

if text == "A":
    score += 5
elif text == "B":
    score += 4
elif text == "C":
    score += 3
elif text == "D":
    score += 1

if role == "A":
    score += 4
elif role == "B":
    score += 3
elif role == "C":
    score += 2
elif role == "D":
    score += 1

if director == "A":
    score += 3
elif director == "B":
    score += 2
elif director == "C":
    score += 1

if cast == "A":
    score += 2
elif cast == "B":
    score += 1

print(score)
if score == "20":
    print("Perfect score")
elif score >= 17:
    print("Must do")
elif score >= 14:
    print("Seriously consider")
elif score >= 12:
    print("On the bubble")
else:
    print("pass")
