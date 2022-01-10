# python3


# def linear_search(keys, query):
#    for i in range(len(keys)):
#        if keys[i] == query:
#            return i
#    return -1


def binary_search(keys, query, l, r):
    # assert all(keys[i] < keys[i + 1] for i in range(len(keys) - 1))
    # assert 1 <= len(keys) <= 3 * 10 ** 4

    # if not keys: return -1
    # low = 0
    # high = len(keys) - 1
    # while low <= high:
    #     mid = low + ((high - low) // 2)
    #     if keys[mid] == query: return mid
    #     if query < keys[mid]:
    #         high = mid - 1
    #     else:
    #         low = mid + 1
    # return -1

    if l > r:
        return -1
    mid = (l + r) // 2
    if query == keys[mid]:
        return mid
    if query < keys[mid]:
        return binary_search(keys, query, l, mid - 1)
    else:
        return binary_search(keys, query, mid + 1, r)


if __name__ == '__main__':
    n = int(input())
    input_keys = list(map(int, input().split()))
    nq = int(input())
    input_queries = list(map(int, input().split()))

    for q in input_queries:
        print(binary_search(input_keys, q, 0, len(input_keys) - 1), end=' ')
