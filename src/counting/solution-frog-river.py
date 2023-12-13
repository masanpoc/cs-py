# use time as index to store positions of leafs


def solution(X, A):
    positions_filled = set()
    time = 0

    # here we have 2 options to loop over:
    # {0...X} implies looping over A to check each value and retrieve index (n2)
    # {a0...aN-1} + implies using in keyword (n), not looping!

    # looping

    for i in range(len(A)):
        if A[i] not in positions_filled:
            positions_filled.add(A[i])
            time = i

    if len(positions_filled) == X:
        return time

    return -1


print(solution(5, [1, 3, 1, 4, 2, 2, 3, 4, 5]))
print(solution(7, [1, 2, 3, 4, 5, 6, 1, 2, 7, 4, 5, 6]))
print(solution(7, [1, 1, 1]))
