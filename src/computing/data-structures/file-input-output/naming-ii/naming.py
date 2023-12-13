# You've been sent a list of names. Unfortunately, the names
# come in two different formats:
#
# First Middle Last
# Last, First Middle
#
# You want the entire list to be the same. For this problem,
# we'll say you want the entire list to be Last, First Middle.
#
# Write a function called name_refixer. name_refixer should have two
# parameters: an output filename (the first parameter) and the
# input filename (the second parameter). You may assume that every
# line will match one of the two formats above: either First Middle
# Last or Last, First Middle.
#
# name_refixer should write to the output file the names all
# structured as Last, First Middle. If the name was already structured
# as Last, First Middle, it should remain unchanged. If it was
# structured as First Middle Last, then Last should be moved
# to the front and a comma should be added after it.
#
# The names should appear in the same order as the original file.
#
# For example, if the input file contained the following lines:
# David Andrew Joyner
# Hart, Melissa Joan
# Cyrus, Billy Ray
#
# ...then the output file should contain these lines:
# Joyner, David Andrew
# Hart, Melissa Joan
# Cyrus, Billy Ray


# Add your code here!
def name_refixer(write_file, read_file):
    try:
        input_file = open(read_file, "r")
        output_file = open(write_file, "w")
        for line in input_file:
            line = line.strip()
            if "," not in line:
                full_name = line.split()
                full_name = f"{full_name[2]}, {full_name[0]} {full_name[1]}"
                print(full_name, file=output_file)
            else:
                print(line, file=output_file)
    except Exception as e:
        print(e)


# The code below will test your function. You can find the two
# files it references in the drop-down in the top left. If your
# code works, output_file.txt should have the text:
# Joyner, David Andrew
# Hart, Melissa Joan
# Cyrus, Billy Ray
name_refixer("output_file.txt", "input_file.txt")
print("Done running! Check output_file.txt for the result.")

# If you accidentally erase input_file.txt, here's its original
# text to copy back in (remove the pound signs):
# David Andrew Joyner
# Hart, Melissa Joan
# Cyrus, Billy Ray
