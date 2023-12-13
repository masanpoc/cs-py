def is_permutation(A):
    non_duplicates = set()
    for i in range(len(A)):
        if A[i] not in non_duplicates:
            non_duplicates.add(A[i])
    if len(non_duplicates) == len(A) and max(A) == len(A) and min(A) == 1:
        return True
    False


def solution(A):
    # check sum is OK and check for duplicates and required min & max
    if (int((len(A) + 1) * len(A)) / 2) == sum(A) and is_permutation(A):
        return True
    return False


# False is 0, True is 1 (remember alphabetically)

print(solution([1, 2, 3, 4]))
print(solution([2, 2, 2, 4, 5, 6]))
print(solution([1, 2, 3, 4, 5, 6]))
print(solution([1, 2, 2, 2]))
print(solution([4, 1, 3]))
print(solution([5, 4, 3, 2, 1]))
