# python3

def fibonacci_number(n):
    if n <= 1:
        return n
    else:
        prev, curr = 0, 1
        for i in range(n-1):
            prev, curr = curr, (prev + curr) % 10
        return curr

def last_digit_of_the_sum_of_fibonacci_numbers_naive(n):
    assert 0 <= n <= 10 ** 18

    if n <= 1:
        return n

    fibonacci_numbers = [0] * (n + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, n + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum(fibonacci_numbers) % 10


def last_digit_of_the_sum_of_fibonacci_numbers(n):
    assert 0 <= n <= 10 ** 18

    prev, curr = 0, 1

    # last digit of fibonacci number repeats after a period of 60
    pisano_period = 60
    n = n % pisano_period
    for i in range(n + 1):
        prev, curr = curr, (prev + curr)
    curr -= 1
    return curr % 10

    # sum_of_n = fibonacci_number(n + 2) - 1
    # return sum_of_n % 10


if __name__ == '__main__':
    input_n = int(input())
    print(last_digit_of_the_sum_of_fibonacci_numbers(input_n))
