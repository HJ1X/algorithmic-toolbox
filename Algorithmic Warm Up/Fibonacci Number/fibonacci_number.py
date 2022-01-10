# python3


def fibonacci_number_naive(n):
    assert 0 <= n <= 45
    if n <= 1:
        return n
    return fibonacci_number_naive(n - 1) + fibonacci_number_naive(n - 2)


def fibonacci_number(n):
    assert 0 <= n <= 10000000000
    if n <= 1:
        return n
    else:
        prev, curr = 0, 1
        for i in range(n-1):
            prev, curr = curr, prev + curr
        return curr


if __name__ == '__main__':
    input_n = int(input())
    print(fibonacci_number(input_n))
