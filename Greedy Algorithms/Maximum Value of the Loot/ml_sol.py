from sys import stdin


def get_optimal_value(capacity, weights, values):
    if capacity == 0: return 0
    lst = []
    for i in range(n):
        v, w = values[i], weights[i]
        if v == 0: continue
        lst.append((v, w))
    lst.sort(key=lambda x: x[0] / x[1], reverse=True)
    total_val = 0
    for v, w in lst:
        if capacity == 0: return total_val
        amt = min(w, capacity)
        total_val += amt * v / w
        capacity -= amt
    return total_val


if __name__ == "__main__":
    data = list(map(int, stdin.read().split()))
    n, input_capacity = data[0:2]
    input_prices = data[2:(2 * n + 2):2]
    input_weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(input_capacity, input_weights, input_prices)
    print(float("{:.10f}".format(opt_value)))
