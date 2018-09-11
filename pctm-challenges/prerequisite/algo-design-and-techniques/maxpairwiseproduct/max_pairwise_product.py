# Uses python3
n = int(input())
numbers = [int(x) for x in input().split()]

# Sanity Test
assert(len(numbers) == n)

def find_largest(arr):
    # selection sort
    largest = arr[0]
    largest_index = 0
    for i in range(1, len(arr)):
        if arr[i] > largest:
            largest = arr[i]
            largest_index = i
    return largest_index

def max_pair(arr):
    new_arr = [None] * 2
    for i in range(0, 2):
        largest = find_largest(arr)
        new_arr[i] = arr.pop(largest)
    return new_arr[0] * new_arr[1]

result = max_pair(numbers)

print(result)
