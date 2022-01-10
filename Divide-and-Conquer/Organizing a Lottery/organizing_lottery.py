# python3
from sys import stdin
from bisect import bisect_left, bisect_right


def points_cover_naive(starts, ends, points):
    assert len(starts) == len(ends)
    count = [0] * len(points)

    for index, point in enumerate(points):
        for start, end in zip(starts, ends):
            if start <= point <= end:
                count[index] += 1

    return count


def points_cover(starts, ends, points):
    # Joining range start and ends
    ranges = []
    for i in range(len(starts)):
        ranges.append([starts[i], 1])         # (l, 1)
        ranges.append([ends[i] + 1, -1])      # (r + 1, -1)

    pts = []
    for i in range(len(points)):
        pts.append([points[i], i])            # mapping points with indexes so that they can be sorted

    ranges.sort()
    pts.sort()

    counts, count = [0] * len(points), 0
    j = 0
    for point in pts:
        x = point[0]
        while j < len(ranges) and ranges[j][0] <= x:
            count += ranges[j][1]
            j += 1
        counts[point[1]] = count

    return counts



if __name__ == '__main__':
    data = list(map(int, stdin.read().split()))
    n, m = data[0], data[1]
    input_starts, input_ends = data[2:2 * n + 2:2], data[3:2 * n + 2:2]
    input_points = data[2 * n + 2:]

    output_count = points_cover(input_starts, input_ends, input_points)
    print(*output_count)
