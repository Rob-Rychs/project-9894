# Uses python3
n = int(input())
numbers = [int(x) for x in input().split()]

# Sanity Test
assert(len(numbers) == n)

def max_pairwise_product(arr):
    largest = arr[0]
    second_largest = arr[1]
    for i in range(1, len(arr)):
        if arr[i] >= second_largest:
            second_largest = arr[i]
        elif arr[i] > largest:
            largest = arr[i]
    return largest * second_largest

result = max_pairwise_product(numbers)

print(result)
