def merge_sort(a):
    n = len(a) - 1
    if n == 0:
        return a, 0
    m = n // 2
    b, b_cnt = merge_sort(a[:m+1])
    c, c_cnt = merge_sort(a[m+1:])
    a_prime, cnt = merge(b, c)
    return a_prime, cnt + b_cnt + c_cnt


def merge(b, c):
    a_prime = []
    count = 0
    while b and c:
        if b[0] > c[0]:
            a_prime.append(c[0])
            count += len(b)
            del c[0]
        else:
            a_prime.append(b[0])
            del b[0]
    return a_prime + b + c, count


if __name__ == '__main__':
    input_n = int(input())
    array = list(map(int, input().split()))
    sorted_array, count = merge_sort(array)
    print(count)