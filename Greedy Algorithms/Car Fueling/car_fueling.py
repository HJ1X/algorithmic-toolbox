# python3


def compute_min_number_of_refills(d, m, stops):
    assert 1 <= d <= 10 ** 5
    assert 1 <= m <= 400
    assert 1 <= len(stops) <= 300
    assert 0 < stops[0] and all(stops[i] < stops[i + 1] for i in range(len(stops) - 1)) and stops[-1] < d

    no_of_refills = 0
    curr_pos = 0

    n = len(stops)
    stops = [0] + stops + [d]  # adding destination to list

    while curr_pos <= n:
        last_refill = curr_pos
        while curr_pos <= n and stops[curr_pos + 1] - stops[last_refill] <= m:
            curr_pos = curr_pos + 1
        if last_refill == curr_pos: return -1
        if curr_pos <= n: no_of_refills += 1
    return no_of_refills


if __name__ == '__main__':
    input_d = int(input())
    input_m = int(input())
    input_n = int(input())
    input_stops = list(map(int, input().split()))
    assert len(input_stops) == input_n

    print(compute_min_number_of_refills(input_d, input_m, input_stops))
