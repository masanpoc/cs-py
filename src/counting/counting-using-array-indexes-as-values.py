# count how many occurrences
# in an array with elements in {0, ..., m}


# use array to store occurrences in index
def counting(A, m):
    n = len(A)
    count = [0] * (m + 1)
    for k in range(n):
        count[A[k]] += 1
    return count


# print(counting([0, 2, 2, 4, 8], 8))
# prints occurrences of values storing them in index position {value}


# A ~= [0, 1, 34, 2, 3, 3, 4]
# B ~= [2, 34, 3, 5, 2, 35, 36]
# m ~= 36


def can_swap(A, B, m):
    n = len(A)
    n = len(B)

    if sum(B) > sum(A):
        C = A
        A = B
        B = C
    # A sum has to meet B sum in a middle, suffering a lost, while B gains a gain
    # to reach this middle point,
    # each array has to gain/loose the substraction of sums divided by 2
    # (if substraction % 2 ==1 return false)
    diff = sum(A) - sum(B)
    if diff % 2 == 1:
        return False
    gain = int(diff / 2)

    # B[match] = A[match] + b_gain
    # A[match] = B[match] - a_loss (b_gain)

    # store occurrences of A in count list
    count = counting(A, m)

    # loop over B
    for i in range(n):
        # check limits first (specially prevent A index error,
        # by checking B is less than m)
        if (B[i] <= m) and ((B[i] - gain) >= 0) and count[B[i] - gain] > 0:
            # matches first, there may be more
            # print("found!", B[i] - gain, B[i], count)
            return True
    return False


print(can_swap([3, 2, 4], [2, 4, 1], 4))
