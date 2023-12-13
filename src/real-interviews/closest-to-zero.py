def compute_closest_to_zer(ts):
    # loop over array & store minimum
    minimum = 10001
    if len(ts) == 0:
        return 0
    for temp in ts:
        if abs(temp) < abs(minimum):
            minimum = temp
        elif abs(temp) == abs(minimum) and temp > 0:
            minimum = temp
    return minimum


print(compute_closest_to_zer([-1, 2, -1, 1]))
print(compute_closest_to_zer([]))
