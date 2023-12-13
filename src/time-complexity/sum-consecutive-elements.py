# find missing num from consecutive integers array
# [1,2,4] -> 3

# remember that the sum of n-1 consecutive numbers has the following expression
# sum = ((n + 1) * n ) / 2


def solution(A):
    # since there is one element missing
    # the correct value for n would be len(A)+1
    n = len(A) + 1
    total = ((n + 1) * n) / 2
    return int(total - sum(A))


print(solution([1, 2, 4]))
