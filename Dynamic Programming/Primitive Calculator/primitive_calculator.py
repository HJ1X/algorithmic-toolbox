# python3


def compute_operations(n):
    assert 1 <= n <= 10 ** 6
    min_op = [0] * (n + 1)
    op_seq = [[i] for i in range(n + 1)]

    for m in range(1, n + 1):
        min_op[m] = float("inf")
        if m % 3 == 0:
            num_op = min_op[m // 3] + 1
            if num_op < min_op[m]:
                min_op[m] = num_op
                op_seq[m] = op_seq[m//3] + op_seq[m]
        if m % 2 == 0:
            num_op = min_op[m // 2] + 1
            if num_op < min_op[m]:
                min_op[m] = num_op
                op_seq[m] = [m]
                op_seq[m] = op_seq[m//2] + op_seq[m]
        num_op = min_op[m - 1] + 1
        if num_op < min_op[m]:
            min_op[m] = num_op
            op_seq[m] = [m]
            op_seq[m] = op_seq[m - 1] + op_seq[m]
    return op_seq[m][1:]


if __name__ == '__main__':
    input_n = int(input())
    output_sequence = compute_operations(input_n)
    print(len(output_sequence) - 1)
    print(*output_sequence)