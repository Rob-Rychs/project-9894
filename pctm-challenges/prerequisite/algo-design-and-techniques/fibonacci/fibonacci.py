# Uses python3

n = int(input())
def fibonacci(n):
    # Sanity Test
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, previous + current

    return current


def get_fibonacci_last_digit_naive(n):
    # Sanity Test
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current % 10, (previous + current) % 10

    return current

print(get_fibonacci_last_digit_naive(n))
