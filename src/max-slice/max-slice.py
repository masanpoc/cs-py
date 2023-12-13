# given [5,-7,3,5,-2,4,-1] -> sum of max slice is 10 ([3,5,-2,4])


# O(n2)
# prefix sum = [5,-2,1,6,4,8,7]
def max_slice(A, pref):
    n = len(A)
    result = 0
    for p in range(n):
        for q in range(p, n):
            # for p=1, q=4 -> sum is 8--2 = 10
            # from X=3 to Y=4
            # from idx=2 to idx=5
            # P[5]-P[2-1] = 8--2 = 10
            # REMEMBER sum of slices:
            # P[y]-P[x-1]
            # or P[y+1]-P[x]
            sum = pref[q + 1] - pref[p]
            result = max(result, sum)
    return result


# O(n2)
def max_slice_without_prefix(A, pref):
    n = len(A)
    result = 0
    for p in range(n):
        sum = 0
        for q in range(p, n):
            sum += A[q]
            result = max(result, sum)
    return result
