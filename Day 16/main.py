import time
from collections import deque

# Read puzzle input data
def readFile(fileName: str):
    with open(fileName, "r") as file:
        data = [list(line.rstrip()) for line in file]
    return data

def findRoutes(maze: list[list[str]]):
    rows, cols = len(maze), len(maze[0])
    start = None
    end = None

    # Search start & end point coordinates
    for r in range(rows):
        for c in range(cols):
            if maze[r][c] == 'S':
                start = (r, c)
            elif maze[r][c] == 'E':
                end = (r, c)
        if start and end:
            break

    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    routes = []
    visited = {}
    queue = deque([(start, [start], 0, 0)])     # (row, col), history, score, direction

    while queue:
        (x, y), history, score, direction = queue.popleft()

        if (x, y) == end:
            routes.append((history, score))
            continue

        if ((x, y), direction) in visited and visited[((x, y), direction)] < score:
            continue

        visited[((x, y), direction)] = score
            

        for next_dir, (dx, dy) in enumerate(dirs):
            nx, ny = x + dx, y + dy
            if 0 <= nx < rows and 0 <= ny < cols and maze[nx][ny] != '#' and (nx, ny) not in history:
                if next_dir == direction:
                    queue.append(((nx, ny), history + [(nx, ny)], score + 1, next_dir))
                else:
                    queue.append(((x, y), history + [], score + 1000, next_dir))

    return routes


def part1(fileName: str):
    _map = readFile(fileName)
    routes = findRoutes(_map)
    min_score = min(route[1] for route in routes)
    print("Part 1:", min_score)


def part2(fileName: str):
    _map = readFile(fileName)
    routes = findRoutes(_map)
    min_score = min(route[1] for route in routes)
    best_routes = [route for route in routes if route[1] == min_score]
    tiles = {tile for route in best_routes for tile in route[0]}
    print("Part 2:", len(tiles))


def main():
    print("Day 16:")
    start_time = time.time()
    part1("input.txt")
    print("--- %s seconds ---" % (time.time() - start_time))

    part2_start_time = time.time()
    part2("input.txt")
    print("--- %s seconds ---" % (time.time() - part2_start_time))


if __name__ == '__main__':
    main()
