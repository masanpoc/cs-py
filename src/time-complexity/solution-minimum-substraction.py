# find the minimum of substractions between sum(A[:i+1]) & sum(A[i:])


def solution(A):
    left_sum = 0
    right_sum = sum(A)
    minimum = float("inf")
    # strategy:
    # start from the beginning
    # sum the i value to the left sum
    # substract the i value for the right sum
    for num in A[:-1]:
        left_sum += num
        right_sum -= num
        minimum = min(abs(right_sum - left_sum), minimum)
    return minimum


print(solution([32, 1, 2, 4, 3]))
print(solution([32, 2]))
print(solution([2, 5, 2, 32, 2]))
