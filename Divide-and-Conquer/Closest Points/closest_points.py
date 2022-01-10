# python3
from collections import namedtuple
from itertools import combinations
from math import sqrt


Point = namedtuple('Point', 'x y')


def distance_squared(first_point, second_point):
    return sqrt((first_point.x - second_point.x) ** 2 + (first_point.y - second_point.y) ** 2)


def minimum_distance_squared_naive(points):
    min_distance_squared = float("inf")

    for p, q in combinations(points, 2):
        min_distance_squared = min(min_distance_squared,
                                   distance_squared(p, q))

    return min_distance_squared


def minimum_distance_squared(points, l, r):
    # base case
    if r - l <= 3:
        return minimum_distance_squared_naive(points[l:r+1])

    mid = (l + r) // 2
    d1 = minimum_distance_squared(points, l, mid)
    d2 = minimum_distance_squared(points, mid + 1, r)
    d = min(d1, d2)

    pts = []
    i = mid
    while i < len(points) and points[i].x - points[mid].x < d:
        pts.append(points[i])
        i += 1
    i = mid - 1
    while i >= 0 and points[mid].x - points[i].x < d:
        pts.append(points[i])
        i -= 1

    pts.sort(key=lambda point: point.y)
    min_val = d                              # initialize min_dist to be d
    for i in range(len(pts)):
        j = i + 1
        while j < len(pts) and pts[j].y - pts[i].y < min_val:
            min_val = distance_squared(pts[i], pts[j])
            j += 1

    return min_val


if __name__ == '__main__':
    input_n = int(input())
    input_points = []
    for _ in range(input_n):
        x, y = map(int, input().split())
        input_point = Point(x, y)
        input_points.append(input_point)
    input_points.sort()
    print("{0:.6f}".format(minimum_distance_squared(input_points, 0, input_n - 1)))
