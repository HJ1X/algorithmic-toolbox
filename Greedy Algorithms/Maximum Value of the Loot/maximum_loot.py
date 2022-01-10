# python3

from sys import stdin


def maximum_loot_value(capacity, weights, prices):
    assert 0 <= capacity <= 2 * 10 ** 6
    assert len(weights) == len(prices)
    assert 1 <= len(weights) <= 10 ** 3
    assert all(0 < w <= 2 * 10 ** 6 for w in weights)
    assert all(0 <= p <= 2 * 10 ** 6 for p in prices)

    val_total = 0

    for j in range(len(weights)):
        if capacity == 0: return val_total
        max_val = 0
        for i in range(len(weights)):
            if weights[i] > 0 and prices[i] / weights[i] > max_val:
                max_index = i
                max_val = prices[i] / weights[i]
        amount = min(capacity, weights[max_index])
        capacity -= amount
        val_total += amount * max_val
        weights[max_index] = 0
    return val_total


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, input_capacity = data[0:2]
    input_prices = data[2:(2 * n + 2):2]
    input_weights = data[3:(2 * n + 2):2]
    opt_value = maximum_loot_value(input_capacity, input_weights, input_prices)
    print(float("{:.10f}".format(opt_value)))
