# Uses python3
import sys
from collections import namedtuple

Segment = namedtuple('Segment', 'start end')

def optimal_points(segments):
    points = []
    list_segments = []
    #write your code here
    for s in segments:
        list_segments.append(s.start)
        list_segments.append(s.end)
    
    
    min_right = 10 ** 10
    position_min_right = 0
    cont_segments = 0
    i = 0

    while i < len(list_segments) and (cont_segments < len(list_segments) / 2):
        for j in range(1, len(list_segments), 2):
            if min_right > list_segments[j]:
                min_right = list_segments[j]
                position_min_right = j

        points.append(min_right)

        for k in range(0, len(list_segments), 2):
            if list_segments[k] <= min_right and min_right <= list_segments[k + 1]:
                list_segments[k] = 10 ** 10
                list_segments[k + 1] = 10 ** 10
                cont_segments += 1

        min_right = 10 ** 10

    return points


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
