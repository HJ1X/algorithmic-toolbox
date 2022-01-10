# python3


def edit_distance(first_string, second_string):
    n = len(first_string)
    m = len(second_string)
    d = [[i for i in range(m + 1)] for i in range(n + 1)]
    for j in range(1, n + 1):
        d[j][0] = j
    for j in range(1, m + 1):
        for i in range(1, n + 1):
            ins = d[i][j - 1] + 1
            dele = d[i - 1][j] + 1
            mismatch = d[i - 1][j - 1] + 1
            match = d[i - 1][j - 1]
            if first_string[i - 1] == second_string[j - 1]:
                d[i][j] = min(ins, dele, match)
            else:
                d[i][j] = min(ins, dele, mismatch)
    return d[n][m]


if __name__ == "__main__":
    print(edit_distance(input(), input()))
