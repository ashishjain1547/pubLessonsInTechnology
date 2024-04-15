def max_slice_sum(arr):
  """
  Finds the maximum sum of a contiguous subarray in a given array.

  Args:
    arr: A list of integers.

  Returns:
    The maximum sum of a contiguous subarray in the array.
  """
  current_sum = max_sum = arr[0]
  for num in arr[1:]:
    current_sum = max(num, current_sum + num)
    max_sum = max(max_sum, current_sum)
  return max_sum

arr = [5, -7, 8, -4, 1]
print(max_slice_sum(arr))  # Output: 8

arr = [5, -7, 3, 5, -2, 4, -1]
print(max_slice_sum(arr))  # Output: 10

arr = [2, 2, -5, 4, 7, 5, 6, 6, 4, -10]
print(max_slice_sum(arr))  # Output: 32 = sum([4, 7, 5, 6, 6, 4])


arr = [8, 8, -5, 1]
print(max_slice_sum(arr))  # Output: 16 = 8+8


arr = [3, 3, -5, 9]
print(max_slice_sum(arr))  # Output: 10 = sum(arr)


arr = [3, 3, -5, 9, 7, 7, 7, 7, -2, 1]
print(max_slice_sum(arr))  # Output: 38 = 10 + 7+7+7+7

arr = [-8, -7, -1, -4, 6, -9, 3, -1, 8, -5]
print(max_slice_sum(arr))  # Output: 10 = sum([3, -1, 8])


import random

# Generate 10 random integers between 0 and 100 (inclusive)
numbers = [random.randint(-10, 10) for _ in range(10)]
print(numbers)




