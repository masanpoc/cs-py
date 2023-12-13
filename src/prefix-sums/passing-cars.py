# calculate pairs of 0-1 in an array, but only consecutive


def prefix_sums(A):
    n = len(A)
    P = [0] * (n)
    P[0] = A[0]
    # k = 1, 2, 3, ... n-1
    for k in range(1, n):
        P[k] = P[k - 1] + A[k]
    return P


def solution(A):
    sums = prefix_sums(A)
    count = 0
    total = sums[len(A) - 1]
    for i in range(len(A) - 1):
        if A[i] == 0:
            # counting all 1s to the right of the given 0
            # (all cars the current car will encounter going east)
            count += total - sums[i]
            if count > 1000000000:
                return -1
    return count


print(solution([1, 1, 0, 1]))
print(solution([0, 1, 0, 1, 1]))
