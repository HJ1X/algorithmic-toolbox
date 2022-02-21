# python3

from itertools import permutations


def largest_number_naive(numbers):
    numbers = list(map(str, numbers))
    largest = 0
    for permutation in permutations(numbers):
        largest = max(largest, int("".join(permutation)))

    return largest


def largest_number(numbers):
    lst = numbers
    answer = []
    while lst:
        max_digit = 0
        for i in lst:
            if int(str(i) + str(max_digit)) >= int(str(max_digit) + str(i)):
                max_digit = i
        answer.append(max_digit)
        lst.remove(max_digit)
    return int("".join([str(i) for i in answer]))


if __name__ == '__main__':
    n = int(input())
    input_numbers = input().split()
    assert len(input_numbers) == n
    print(largest_number(input_numbers))
