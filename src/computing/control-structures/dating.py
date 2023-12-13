years = 2
months = 5
days = 24

#
# - If you've been dating for at least 4 years, give them a
#   dog ("dog").
# - If you've been dating for at least 1 year but less than
#   4 years, give them a watch ("watch").
# - If you've been dating for at least 6 months but less than
#   1 year, give them concert tickets ("concert tickets").
# - If you've been dating for at least a day but less than 6
#   months, give them candy ("candy").
# - If aren't actually dating, go big or go home: give them
#   a yacht to sail away together ("yacht").
#
# Note that no matter what, you should only print one gift.

if years >= 4:
    print("dog")
elif years >= 1:
    print("watch")
elif months >= 6:
    print("concert tickets")
elif days >= 1:
    print("candy")
else:
    print("yatch")
