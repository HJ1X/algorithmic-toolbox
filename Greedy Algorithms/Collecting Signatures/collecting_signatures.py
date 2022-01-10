# python3

from collections import namedtuple
from sys import stdin

Segment = namedtuple('Segment', 'start end')


def compute_optimal_points(segments):
    # segments_copy = segments[:]
    # meet_points = []
    # segments_copy.sort()
    # while segments_copy != []:
    #     index_to_remove = 0
    #     point = segments_copy[0][1]
    #     for i in range(1, len(segments_copy)):
    #         if segments_copy[i][0] <= point:
    #             index_to_remove = i
    #             point = min(point, segments_copy[i][1])
    #         else: break
    #     meet_points.append(point)
    #     del segments_copy[:index_to_remove + 1]
    # return meet_points

    segments.sort()
    i = 0
    points = []
    while i < len(segments):
        point = segments[i][1]
        i += 1
        while i < len(segments) and segments[i][0] <= point:
            point = min(point, segments[i][1])
            i += 1
        points.append(point)
    return points


if __name__ == '__main__':
    n, *data = map(int, stdin.read().split())
    input_segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    assert n == len(input_segments)
    output_points = compute_optimal_points(input_segments)
    print(len(output_points))
    print(*output_points)
