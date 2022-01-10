# python3


def last_digit_of_the_sum_of_fibonacci_numbers_again_naive(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18

    if to_index == 0:
        return 0

    fibonacci_numbers = [0] * (to_index + 1)
    fibonacci_numbers[0] = 0
    fibonacci_numbers[1] = 1
    for i in range(2, to_index + 1):
        fibonacci_numbers[i] = fibonacci_numbers[i - 2] + fibonacci_numbers[i - 1]

    return sum(fibonacci_numbers[from_index:to_index + 1]) % 10


def last_digit_of_the_sum_of_fibonacci_numbers_again(from_index, to_index):
    assert 0 <= from_index <= to_index <= 10 ** 18

    prev_t, curr_t = 0, 1
    prev_f, curr_f = 0, 1
    pisano_period = 60
    from_index, to_index = from_index % pisano_period, to_index % pisano_period
    for i in range(to_index + 1):
        prev_t, curr_t = curr_t, (prev_t + curr_t)
    for i in range(from_index):
        prev_f, curr_f = curr_f, (prev_f + curr_f)
    # curr_t %= 10
    # curr_f %= 10
    # if curr_f > curr_t: curr_t += 10

    return curr_t - curr_f


if __name__ == '__main__':
    input_from, input_to = map(int, input().split())
    print(last_digit_of_the_sum_of_fibonacci_numbers_again(input_from, input_to))
