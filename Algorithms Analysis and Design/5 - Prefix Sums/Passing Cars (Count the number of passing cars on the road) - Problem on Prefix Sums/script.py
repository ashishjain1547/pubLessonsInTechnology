def solution(A):
    # In the question, it is given that 0 are travelling east. We assume it to be the direction of prefix sums.
    # So if we implement using prefix counts, we would have to count zeroes.

    # '1' is going to the west, that is having the direction of suffix sums.
    
    prefix_counts = [0] * (len(A) + 1)

    for i in range(len(A)):
        if A[i] == 0:
            prefix_counts[i+1] = prefix_counts[i] + 1
        else:
            prefix_counts[i+1] = prefix_counts[i] + 0

    passing_cars = 0 
    for i in range(len(A)):
        if A[i] == 1:
            passing_cars += prefix_counts[i+1]

    if passing_cars > 1000000000:
        passing_cars = -1

    return passing_cars


# NOW USING SUFFIX SUMS

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # In the question, it is given that 0 are travelling east. We assume it to be the direction of prefix sums.

    # '1' is going to the west, that is having the direction of suffix sums.
    # So if we implement using suffix counts, we would have to count ones.
    
    suffix_counts = [0] * (len(A) + 1)

    for i in range(len(A) - 1, -1, -1):
        if A[i] == 1:
            suffix_counts[i] = suffix_counts[i+1] + 1
        else:
            suffix_counts[i] = suffix_counts[i+1] + 0

    passing_cars = 0 
    for i in range(len(A)):
        if A[i] == 0:
            passing_cars += suffix_counts[i]

    if passing_cars > 1000000000:
        passing_cars = -1

    return passing_cars

