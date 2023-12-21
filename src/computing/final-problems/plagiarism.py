# A common problem in academic settings is plagiarism
# detection. Fortunately, software can make this pretty easy!
#
# In this problem, you'll be given two files with text in
# them. Write a function called check_plagiarism with two
# parameters, each representing a filename. The function
# should find if there are any instances of 5 or more
# consecutive words appearing in both files. If there are,
# return the longest such string of words (in terms of number
# of words, not length of the string). If there are not,
# return the boolean False.
#
# For simplicity, the files will be lower-case text and spaces
# only: there will be no punctuation, upper-case text, or
# line breaks.
#
# We've given you three files to experiment with. file_1.txt
# and file_2.txt share a series of 5 words: we would expect
# check_plagiarism("file_1.txt", "file_2.txt") to return the
# string "if i go crazy then". file_1.txt and file_3.txt
# share two series of 5 words, and one series of 11 words:
# we would expect check_plagiarism("file_1.txt", "file_3.txt")
# to return the string "i left my body lying somewhere in the
# sands of time". file_2.txt and file_3.txt do not share any
# text, so we would expect check_plagiarism("file_2.txt",
# "file_3.txt") to return the boolean False.
#
# Be careful: there are a lot of ways to do this problem, but
# some would be massively time- or memory-intensive. If you
# get a MemoryError, it means that your solution requires
# storing too much in memory for the code to ever run to
# completion. If you get a message that says "KILLED", it
# means your solution takes too long to run.

import traceback


# Add your code here!
def check_plagiarism(input_filename, source_filename):
    try:
        input_file = open(input_filename, mode="r")
        source_file = open(source_filename, mode="r")

        input_data = input_file.read().split()
        source_data = source_file.read().split()

        plagiarized_list = []
        covered_indexes = []

        for i in range(len(input_data) - 4):
            word = input_data[i]

            if word in source_data and i not in covered_indexes:
                j = 0
                is_plagiarism = None

                if source_data.count(word) > 1:
                    copy = source_data
                    is_plagiarism = False
                    times = 0

                    while copy.count(word) > 0:
                        j2 = copy.index(word)
                        j += j2

                        if j2 + 4 >= len(copy):
                            break

                        if input_data[i + 4] == copy[j2 + 4]:
                            is_plagiarism = True
                            j = j + times

                            break

                        copy = copy[(j2 + 1) :]
                        times += 1
                else:
                    j = source_data.index(word)

                    if j + 4 >= len(source_data):
                        continue

                    if input_data[i + 4] == source_data[j + 4]:
                        is_plagiarism = True

                if is_plagiarism:
                    plagiarized_el = []
                    same_data = True
                    idx_diff = 0

                    while same_data:
                        plagiarized_el.append(input_data[i + idx_diff])
                        idx_diff += 1
                        covered_indexes.append(i + idx_diff)

                        if input_data[i + idx_diff] != source_data[j + idx_diff]:
                            same_data = False

                    if len(plagiarized_el) > 0:
                        plagiarized_list.append(plagiarized_el)

        input_file.close()
        source_file.close()

        if len(plagiarized_list) > 0:
            final = plagiarized_list[0]

            for sentence in plagiarized_list:
                if len(sentence) > len(final):
                    final = sentence

            return " ".join(final)

        return False

    except Exception as error:
        print(traceback.format_exc())


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print:
# if i go crazy then
# i left my body lying somewhere in the sands of time
# False
print(check_plagiarism("file_1.txt", "file_2.txt"))
print(check_plagiarism("file_1.txt", "file_3.txt"))
print(check_plagiarism("file_2.txt", "file_3.txt"))
