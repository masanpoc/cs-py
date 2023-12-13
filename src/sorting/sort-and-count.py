# most used orders = numerical & alphabetical


# n2
def selectionSort(A):
    n = len(A)
    for k in range(n):
        minimal = k
        for j in range(k + 1, n):
            if A[j] < A[minimal]:
                minimal = j
        # swap A[k] and A[minimal] for k iteration
        A[k], A[minimal] = A[minimal], A[k]
    return A


# eg: [3,2,1]
# k=1 -> [1,2,3]
# k=2 -> [1,2,3]


# n+k
# k = limit range of values
def countingSort(A, k):
    n = len(A)
    count = [0] * (k + 1)
    for i in range(n):
        # increasing occurrence for index as value
        count[A[i]] += 1
    p = 0
    # iterating through counters array [0, 5, 0, 0, 1] (from A=[1,1,4,1,1,1])
    for i in range(k + 1):
        # for each value
        for j in range(count[i]):
            # for each occurrence
            A[p] = i
            # increase p to store a value in the next position
            # eg [0,5,0,0,1] -> [1xp=5, 4]
            p += 1
    return A


# log n
# merge sort -> [1,3,4,2] -> [1,3] + [4,2] -> [1,3] + [2,4] -> [1,2,3,4]

# n logn
# A.sort()
# built-in sorting (implementation faster, readability increased)


# return count of unique numbers in A
def distinct(A):
    n = len(A)
    A.sort()
    result = 1
    for k in range(1, n):
        # if value is the same as prior -> do nothing
        # else -> increase count of unique values
        if A[k] != A[k - 1]:
            result += 1
    return result


print(distinct([1, 2, 2, 1, 1, 4]))
