mystery_string = "my cat your cat"

# Add some code below that will count and print how many
# times the character sequence "cat" appears in mystery_string.
# For example, for the string above, it would print 2.
#
# This one is tricky! Think carefully about for-each loops,
# conditionals, and booleans. How can you track what character
# you're currently looking for? We expect you'll use a loop
# and a single big conditional, but there are other approaches
# as well. Try to stick with the topics we've covered so far.


# Add your code here!
counter = 0

for char_idx in range(len(mystery_string) - 2):
    if (
        mystery_string[char_idx] == "c"
        and mystery_string[char_idx + 1] == "a"
        and mystery_string[char_idx + 2] == "t"
    ):
        counter += 1

print(counter)
