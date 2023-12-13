# what occurrences are not odd?
# [1,2,2] -> 1

# just use a dictionary to count occurrences
# and then loop over the keys & values of that dictionary


def solution(A):
    # loop over array
    mydict = dict()
    for num in A:
        if num not in mydict:
            mydict[num] = 1
            continue
        mydict[num] += 1
    # build a dictionary with value as key and number of occurrences as value
    # loop over dict and if v % 2 = 1 -> return v
    for k, v in mydict.items():
        print(k, v)
        if (v % 2) == 1:
            print("mathc!")
            return k
    print(mydict)


print(solution([1, 3, 43, 3, 1, 567, 2, 567, 2, 1, 3, 1, 3]))
