# Uses python3
import unittest

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


class MyTest(unittest.TestCase):
    def test_naive(self):
        self.assertEqual(get_fibonacci_last_digit_naive(3), 2)
        self.assertEqual(get_fibonacci_last_digit_naive(331), 9)
        self.assertEqual(get_fibonacci_last_digit_naive(327305), 5)

    def test_fast(self):
        self.assertEqual(fibonacci(3), 2)

if __name__ == '__main__':
    # unittest.main()
    n = int(input())
    print(fibonacci(n))
