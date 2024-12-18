import time
from collections import deque

# Read puzzle input data
def readFile(fileName: str):
    with open(fileName, "r") as file:
        data = [tuple(map(int, line.rstrip().split(","))) for line in file]
    return data


def bfs(_map: list[list[int]], end):
    rows, cols = len(_map), len(_map[0])
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    visited = set((0, 0))
    queue = deque([((0, 0), 0)])

    while queue:
        (x, y), dist = queue.popleft()

        if (x, y) == end:
            return dist

        for dx, dy in dirs:
            nx = x + dx
            ny = y + dy
            if 0 <= nx < cols and 0 <= ny < rows and _map[ny][nx] != '#' and (nx, ny) not in visited:
                visited.add((nx, ny))
                queue.append(((nx, ny), dist + 1))

    return -1


def fillGrid(grid: list[list[str]], bytes: list[tuple], number: int):
    for i in range(number):
        x, y = bytes[i]
        grid[y][x] = '#'


def part1(fileName: str):

    bytes = readFile(fileName)
    wide = 71
    height = 71

    grid = [['.' for x in range(wide)] for y in range(height)]
    fillGrid(grid, bytes, 1024)
    dist = bfs(grid, (wide - 1, height - 1))
    
    # [print(''.join(line)) for line in grid]

    print("Part 1:", dist)


def part2(fileName: str):

    bytes = readFile(fileName)
    wide = 71
    height = 71
    dist = 0
    nByte = 0

    grid = [['.' for x in range(wide)] for y in range(height)]
    
    while(True):
        x, y = bytes[nByte]
        grid[y][x] = '#'
        if bfs(grid, (wide - 1, height - 1)) == -1:
            break
        nByte += 1

    print("Part 2:", bytes[nByte])


def main():
    print("Day 18:")
    start_time = time.time()
    part1("input.txt")
    print("--- %s seconds ---" % (time.time() - start_time))

    part2_start_time = time.time()
    part2("input.txt")
    print("--- %s seconds ---" % (time.time() - part2_start_time))


if __name__ == '__main__':
    main()
