# leader of array (occurrence > n/2)
# O(n·logn)
def fastLeader(A):
    n = len(A)
    leader = -1
    A.sort()
    candidate = A[n // 2]
    count = 0
    for i in range(n):
        if A[i] == candidate:
            count += 1
    if count > n // 2:
        leader = candidate
    return leader


# O(n)
def goldenLeader(A):
    n = len(A)
    # just start a counter for each element & compare with the rest
    size = 0
    # we obtain either a leader or a random num
    for i in range(n):
        if size == 0:
            size += 1
            value = A[i]
        else:
            if value == A[i]:
                size += 1
            else:
                size -= 1
    if size > 0:
        candidate = value
    leader = -1
    count = 0
    # we count the occurrences for candidate
    for k in range(n):
        if A[k] == candidate:
            count += 1
    if count > (n // 2):
        leader = candidate
    return leader
