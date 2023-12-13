# to do

# families [A, C, C, A, A]
# sizes    [6, 2, 3, 1, 4]

# microorganism eats others smaller & different

# Nmax = 20
# iteration 1
# [A, C, A]
# [8, 4, 4]

# iteration 2
# [A, A]
# [12, 4]

# return 'A 12'

# bamcos alimerntacion farmaceuticos
#
# feedback 1 manager
# fefefefeef


def is_growing(families):
    sorted_families = sorted(families)
    if sorted_families[0] != sorted_families[len(sorted_families) - 1]:
        return True
    else:
        return False


def can_eat_right(families, sizes, i):
    # if sizes[i + 1] == 0:
    #     return False
    if families[i] != families[i + 1] and sizes[i] > sizes[i + 1]:
        return True
    else:
        return False


def can_eat_left(families, sizes, i):
    # check if other neighbour already eat the left one
    if sizes[i - 1] == 0:
        return False
    elif families[i] != families[i - 1] and sizes[i] > sizes[i - 1]:
        return True
    else:
        return False


def solve(families, sizes):
    while is_growing(families):
        # start iterating over microorganisms
        for i in range(len(families)):
            # check if eaten
            if sizes[i] == 0:
                continue

            # eat right except last position
            if i != (len(families) - 1) and can_eat_right(families, sizes, i):
                # if it can eat the right neighbour, ie different & smaller
                # sum the size of neighbour
                sizes[i] += sizes[i + 1]
                sizes[i + 1] = 0
                families[i + 1] = ""

            # eat left except first position
            if i != 0 and can_eat_left(families, sizes, i):
                # if it can eat the left neighbour
                sizes[i] += sizes[i - 1]
                sizes[i - 1] = 0
                families[i - 1] = ""
        # filter out eaten microorganisms

        families = list(filter(lambda x: x != "", families))
        sizes = list(filter(lambda z: z != 0, sizes))

    idx_result = sizes.index(max(sizes))
    return f"{families[idx_result]} {sizes[idx_result]}"


print(solve(["A", "C", "C", "A", "A"], [6, 2, 3, 1, 4]))
