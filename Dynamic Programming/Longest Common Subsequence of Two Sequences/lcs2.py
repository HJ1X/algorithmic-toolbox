# python3


def lcs2(first_sequence, second_sequence):
    assert len(first_sequence) <= 100
    assert len(second_sequence) <= 100

    dp = [[0 for i in range(len(second_sequence) + 1)] for j in range(len(first_sequence) + 1)]

    for i in range(1, len(first_sequence) + 1):
        for j in range(1, len(second_sequence) + 1):
            if first_sequence[i - 1] == second_sequence[j - 1]:
                dp[i][j] = 1 + dp[i-1][j-1]

            else:
                x = dp[i-1][j]
                y = dp[i][j-1]
                dp[i][j] = max(x, y)

    return dp[len(first_sequence)][len(second_sequence)]


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    print(lcs2(a, b))
