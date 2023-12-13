# print("this is a debug message")
# 1 rotation = [1,2,3] -> [3,1,2]


def solution(A, K):
    # rotate K times
    # i = K
    if len(A) == 0:
        rotated_arr = A
    elif K < len(A):
        items_rotating = A[-K:]
        items_stable = A.copy()[:-K]
        rotated_arr = items_rotating + items_stable
    # sol1 - basic
    else:
        rotated_arr = A.copy()
        i = K
        # no need to use a while loop
        # goal for for this lesson was looping
        # apply division and product operations for more efficiency
        while i > 0:
            # store popped item from list in a variable
            tmp = rotated_arr[-1]
            rotated_arr.pop()
            # append it to A
            rotated_arr.insert(0, tmp)
            print(f"iteration {i}", tmp)
            i -= 1

    return rotated_arr


# test1
# print("test1")
print("received output:", solution([3, 8, 9, 7, 6], 7))
print("expected output: ", ["-", 6, "-", "-", "-"])
print(solution([], 3))
