import time
from collections import defaultdict
from math import log10, floor

# Read puzzle input data
def readFile(fileName: str):
    with open(fileName, "r") as file:
        data = [list(map(int, line.rstrip())) for line in file]
    return data


def bfs(_map: list[list[int]], xInit, yInit):
    rows, cols = len(_map), len(_map[0])
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    visited = []
    queue = [(xInit, yInit)]

    while queue:
        x, y = queue.pop()
        for dx, dy in dirs:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < cols and 0 <= ny < rows and (_map[y][x] + 1) == _map[ny][nx]:
                if _map[ny][nx] == 9:
                    visited.append((nx,ny))
                else:
                    queue.append((nx,ny))
    return visited


def part1(fileName: str):

    _map = readFile(fileName)
    rows, cols = len(_map), len(_map[0])
    trailheads = 0

    for row in range(rows):
        for col in range(cols):
            if _map[row][col] == 0:
                visitedPoins = bfs(_map, col, row)
                trailheads += len(set(visitedPoins))

    print("Part 1:", trailheads)


def part2(fileName: str):

    _map = readFile(fileName)
    rows, cols = len(_map), len(_map[0])
    trailheads = 0

    for row in range(rows):
        for col in range(cols):
            if _map[row][col] == 0:
                visitedPoins = bfs(_map, col, row)
                trailheads += len(visitedPoins)

    print("Part 2:", trailheads)


def main():
    print("Day 9:")
    start_time = time.time()
    part1("input.txt")
    print("--- %s seconds ---" % (time.time() - start_time))

    part2_start_time = time.time()
    part2("input.txt")
    print("--- %s seconds ---" % (time.time() - part2_start_time))


if __name__ == '__main__':
    main()
