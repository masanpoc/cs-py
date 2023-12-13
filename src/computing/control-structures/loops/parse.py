flips = "HHTTHTHHTTHHTHTHTHHTTHH"

# The string above gives the results of a series of coin flips,
# H for heads and T for tails.
#
# Count the number of heads and number of tails. Then, print
# a message like this one based on the results:
#
# 13 heads, 10 tails. Heads wins.
#
# Replace 13 and 10 with the actual numbers of heads and tails.
# Replace 'Heads wins.' with 'Tails wins.' ift there are more
# tails, or with 'It's a tie.' if there are the same number of
# heads and tails.
#
# For example:
#
# "HHTTHH" -> 4 heads, 2 tails. Heads wins.
# "THTHTT" -> 2 heads, 4 tails. Tails wins.
# "TTHHHT" -> 3 heads, 3 tails. It's a tie.

t_count = 0
h_count = 0

for char in flips:
    if char == "T":
        t_count += 1
    else:
        h_count += 1

if t_count > h_count:
    winner = "Tails wins."
elif t_count < h_count:
    winner = "Heads wins."
else:
    winner = "It's a tie."

print(f"{h_count} heads, {t_count} tails. {winner}")
