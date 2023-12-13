def next_sell(A, i, n):
    if len(A) <= i + 2:
        return (max(A[i:]), n + 1)
    if (A[i + 1] > A[i]) and (A[i + 2] < A[i + 1]):
        return (A[i + 1], n + 1)
    return next_sell(A, i + 1, n + 1)


def next_buy(A, i, n):
    if len(A) <= i + 2:
        return (0, len(A))
    if A[i] < A[i + 1] and A[i + 1] > A[i + 2]:
        print(A[i])
        return (-A[i], n)

    return next_buy(A, i + 1, n + 1)


def solution(A):
    i = 0
    finances = list()
    holding = True
    while i < len(A):
        if holding:
            (amount, position) = next_sell(A, i, 0)
            finances.append(amount)
            holding = False
            i += position
            continue
        else:
            (amount, position) = next_buy(A, i, 0)
            finances.append(amount)
            holding = True
            i += position
    return sum(finances)


# print(solution([3, 2, 203, 1, 200, 202, 203]))
# print(solution([1, 1, 1, 4, 1, 2, 1]))
