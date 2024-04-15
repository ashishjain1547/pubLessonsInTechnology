def golden_max_slice(A):
    max_ending = max_slice = 0
    for a in A:
        max_ending = max(0, max_ending + a)
        max_slice = max(max_slice, max_ending)
    return max_slice

arr = [5, -7, 8, -4, 1]
print(golden_max_slice(arr))  # Output: 8

arr = [5, -7, 3, 5, -2, 4, -1]
print(golden_max_slice(arr))  # Output: 10

arr = [2, 2, -5, 4, 7, 5, 6, 6, 4, -10]
print(golden_max_slice(arr))  # Output: 32