# Write a function called get_grade that will read a
# given .cs1301 file and return the student's grade.
# To do this, we would recommend you first pass the
# filename to your previously-written reader() function,
# then use the list that it returns to do your
# calculations. You may assume the file is well-formed.
#
# A student's grade should be 100 times the sum of each
# individual assignment's grade divided by its total,
# multiplied by its weight. So, if the .cs1301 just had
# these two lines:
#
# 1 exam_1 80 100 0.6
# 2 exam_2 30 50 0.4
#
# Then the result would be 72:
#
# (80 / 100) * 0.6 + (30 / 50) * 0.4 = 0.72 * 100 = 72


# Write your function here!
def reader(filename):
    try:
        input_file = open(filename, "r")
        file_data = list()
        for line in input_file:
            line.strip()
            line = line.split()
            file_data.append(
                (int(line[0]), line[1], int(line[2]), int(line[3]), float(line[4]))
            )
        input_file.close()
        return file_data
    except Exception as e:
        print(e)


def get_grade(filename):
    file_data = reader(filename)
    grade = 0
    for value in file_data:
        grade += value[2] / value[3] * value[4]
    return grade * 100


# Below are some lines of code that will test your function.
# You can change the value of the variable(s) to test your
# function with different inputs.
#
# If your function works correctly, this will originally
# print: 91.55
print(get_grade("sample.cs1301"))
