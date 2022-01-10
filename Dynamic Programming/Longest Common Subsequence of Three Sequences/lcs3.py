# python3

# def lcs_tab_print(str1, str2):
#     dp = [[[0, []] for i in range(len(str2) + 1)] for j in range(len(str1) + 1)]
#
#     for i in range(1, len(str1) + 1):
#         for j in range(1, len(str2) + 1):
#             if str1[i - 1] == str2[j - 1]:
#                 dp[i][j][0] = 1 + dp[i - 1][j - 1][0]
#                 lst = dp[i-1][j-1][1].copy()
#                 if not lst:
#                     dp[i][j][1] = [[str1[i-1]]]
#                     continue
#                 for k in lst:
#                     k.append(str1[i-1])
#                 dp[i][j][1] = lst
#                     # += dp[i-1][j-1][1] + [str1[i-1]]
#
#             else:
#                 x = dp[i - 1][j][0]
#                 x_str = dp[i - 1][j][1]
#                 y = dp[i][j - 1][0]
#                 y_str = dp[i][j - 1][1]
#                 if x == y:
#                     dp[i][j][0] = x
#                     if len(x_str) == len(y_str):
#                         dp[i][j][1] = x_str + y_str
#                     elif len(x_str) > len(y_str):
#                         dp[i][j][1] = x_str
#                     else:
#                         dp[i][j][1] = y_str
#                 elif x > y:
#                     dp[i][j][0], dp[i][j][1] = x, x_str
#                 else:
#                     dp[i][j][0], dp[i][j][1] = y, y_str
#
#     return dp[len(str1)][len(str2)][0], dp[len(str1)][len(str2)][1]
#
#
# def lcs_memoization(dp, str1, str2, i, j):
#     if i == len(str1) or j == len(str2):
#         return 0
#
#     # If elements are same in two strings just add 1 to count and find lcs by removing those elements from both
#     # strings, i.e. i-1 and i-2
#     if str1[i] == str2[j]:
#         if dp[i + 1][j + 1] is None:
#             dp[i + 1][j + 1] = lcs_memoization(dp, str1, str2, i + 1, j + 1)
#         return dp[i + 1][j + 1] + 1
#
#     # If elements are not equal then, just find max of both strings removing one element from 1 string at a
#     # time, i.e. max(lcs(i-1, j), lcs(i, j-1))
#     else:
#         if dp[i][j + 1] is None:
#             dp[i][j + 1] = lcs_memoization(dp, str1, str2, i, j + 1)
#         if dp[i + 1][j] is None:
#             dp[i + 1][j] = lcs_memoization(dp, str1, str2, i + 1, j)
#         return max(dp[i][j + 1], dp[i + 1][j])
import random


def lcs3_memo(dp, lst1, lst2, lst3, i, j, k):
    if i == len(lst1) or j == len(lst2) or k == len(lst3):
        return 0

    if dp[i][j][k] is not None:
        return dp[i][j][k]

    if lst1[i] == lst2[j] and lst2[j] == lst3[k]:
        dp[i][j][k] = 1 + lcs3_memo(dp, lst1, lst2, lst3, i+1, j+1, k+1)
        return dp[i][j][k]

    else:
        x = lcs3_memo(dp, lst1, lst2, lst3, i, j, k+1)
        y = lcs3_memo(dp, lst1, lst2, lst3, i, j+1, k)
        z = lcs3_memo(dp, lst1, lst2, lst3, i+1, j, k)
        max_lcs = max(x, y, z)
        dp[i][j][k] = max_lcs
        return max_lcs


def lcs3(first_sequence, second_sequence, third_sequence):
    assert len(first_sequence) <= 100
    assert len(second_sequence) <= 100
    assert len(third_sequence) <= 100

    dp = [[[None for i in range(len(third_sequence) + 1)]
           for j in range(len(second_sequence) + 1)]
          for k in range(len(first_sequence) + 1)]

    return lcs3_memo(dp, first_sequence, second_sequence, third_sequence, 0, 0, 0)


if __name__ == '__main__':
    n = int(input())
    a = list(map(int, input().split()))
    assert len(a) == n

    m = int(input())
    b = list(map(int, input().split()))
    assert len(b) == m

    q = int(input())
    c = list(map(int, input().split()))
    assert len(c) == q

    print(lcs3(a, b, c))
