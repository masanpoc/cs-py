# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
# import datetime

# min of jumps from X to Y, each jump = D


def solution(X, Y, D):
    # check for corner cases, eg: jump not needed
    if X == Y:
        return 0
    # it is a simple division!
    jumps = (Y - X) // D
    remainder = (Y - X) % D
    return jumps if remainder == 0 else jumps + 1


# print(solution(10, 85, 30))
print(solution(1, 1000000000, 2))
print(solution(1324, 1000000000, 222))
