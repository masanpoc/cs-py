# obtain the prefix of sums for a given array
def prefix_sums(A):
    n = len(A)
    P = [0] * (n + 1)
    for k in range(1, n + 1):
        P[k] = P[k - 1] + A[k - 1]
    return P


# ie. if A = [2,4,7,1,1,3,2]
# P=[2,6,13,14,15,18,20]
# use prefixes instead of calculating 1 by 1:
# [2, 4+2=6, 6+7=13...]

# for a given P
# if x=7 & y = 3
# the total of sums from 7 to 2 is
# P[idx_y] - P[idx_x-1]
# 18-6 = 12
# now imagine if there are soooo many values to loop over from x to y
# it might be more efficient to calculate the sum of prefixes once,
#  instead of calculating between indexes N times


def count_total(P, x, y):
    return P[y + 1] - P[x]


def mushrooms(A, k, m):
    n = len(A)
    result = 0
    # calculating the prefix sums of full array
    pref = prefix_sums(A)
    # start looping from k to left position extreme, extreme-1...
    for p in range(min(m, k) + 1):
        # obtain possible left moves
        # (extreme left is either all moves m, or k to prevent reaching 0)
        # eg: left_pos = 3, 3-1, 3-2, 3-3 (not -1, -2)
        left_pos = k - p
        right_pos = min(n - 1, max(k, k + m - 2 * p))
        result = max(result, count_total(pref, left_pos, right_pos))
    # now loop from k until right position extreme, extreme-1...
    for p in range(min(m + 1, n - k)):
        right_pos = k + p
        left_pos = max(0, min(k, k - (m - 2 * p)))
        result = max(result, count_total(pref, left_pos, right_pos))
    return result


# testing vals
# k is position
# m is moves
print(mushrooms([2, 3, 7, 5, 1, 3, 9], 4, 6))
