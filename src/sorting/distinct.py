def solution(A):
    n = len(A)
    A.sort()
    if n == 0:
        return -1
    unique_count = 1
    for i in range(1, n):
        if A[i] != A[i - 1]:
            unique_count += 1
    return unique_count


print(solution([2, 1, 1, 2, 3, 3, 1]))
