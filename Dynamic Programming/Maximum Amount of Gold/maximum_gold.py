# python3

from sys import stdin


def maximum_gold(capacity, items):
    assert 1 <= capacity <= 10 ** 4
    assert 1 <= len(items) <= 10 ** 3
    assert all(1 <= w <= 10 ** 5 for w in items)

    dp = [[0 for i in range(capacity + 1)] for j in range(len(items) + 1)]
    for i in range(1, len(items) + 1):
        for w in range(1, capacity + 1):
            dp[i][w] = dp[i-1][w]
            if items[i-1] <= w:
                w_i = items[i-1]
                val = dp[i-1][w-w_i] + w_i         # Adding w_i because weight is equal to value in given problem
                if val > dp[i][w]:
                    dp[i][w] = val

    return dp[len(items)][capacity]


if __name__ == '__main__':
    input_capacity, n, *input_weights = list(map(int, stdin.read().split()))
    assert len(input_weights) == n

    print(maximum_gold(input_capacity, input_weights))
