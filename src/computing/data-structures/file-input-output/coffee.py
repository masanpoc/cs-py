# Write a function called "find_coffee" that expects a
# filename as a parameter. The function should open the
# given file and return True if the file contains the word
# "coffee". Otherwise, the function should return False.
#
# Hint: look up the read() method if you want to do this
# more simply than you might do with readline().


# Write your function here!
def find_coffee(filename):
    try:
        input_file = open(filename, "r")
        content = input_file.read()
        input_file.close()
        if "coffee" in content:
            return True
        else:
            return False

    except Exception as error:
        print(error)


# You can test your function with the provided files named
# "coffeeful.txt" and "coffeeless.txt". With their original
# text, the lines below should print True, then False. You
# may also edit the files by selecting them in the drop
# down in the top left to try your code with different
# input.
print(find_coffee("coffeeful.txt"))
print(find_coffee("coffeeless.txt"))
