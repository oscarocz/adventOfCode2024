import time
from math import fmod

# Read puzzle input data
def readFile(fileName: str):
    robots = []
    with open(fileName, "r") as file:
        for line in file:
            a, b = line.rstrip("\n").split(" ")
            x, y = map(int, a[2:].split(","))
            vx, vy = map(int, b[2:].split(","))
            robots.append(((x, y), (vx, vy)))
    return robots


def part1(fileName: str):
    robots = readFile(fileName)

    wide = 101
    tall = 103
    seconds = 100
    robot_pos = []
    quadrants = [0, 0, 0, 0]
    grid = [['.' for x in range(wide)] for y in range(tall)]

    middle_row = tall // 2
    middle_col = wide // 2

    for robot in robots:
        start_x, start_y = robot[0]
        vx, vy = robot[1]
        x = int(fmod(start_x + vx * seconds, wide))
        y = int(fmod(start_y + vy * seconds, tall))
        if x < 0:
            x += wide
        if y < 0:
            y += tall

        # Avoid robots at the cross of quadrants
        if x == middle_col or y == middle_row:
            continue
        
        quadrant_idx =  int(x > middle_col) + (int(y > middle_row) * 2)
        quadrants[quadrant_idx] += 1

        robot_pos.append((x, y))
        
        if grid[y][x] != '.':
            grid[y][x] += 1
        else:
            grid[y][x] = 1

    

    for line in grid:
        string = "".join(str(char) for char in line)
        print(string)

    print("Part 1:", quadrants[0] * quadrants[1] * quadrants[2] * quadrants[3])


def searchPattern(robots: list, seconds: int):
    wide = 101
    tall = 103
    robot_pos = []
    grid = [['.' for x in range(wide)] for y in range(tall)]

    for robot in robots:
        start_x, start_y = robot[0]
        vx, vy = robot[1]
        x = int(fmod(start_x + vx * seconds, wide))
        y = int(fmod(start_y + vy * seconds, tall))
        if x < 0:
            x += wide
        if y < 0:
            y += tall
        
        if (x, y) in robot_pos:
            return False

        robot_pos.append((x, y))
        
        if grid[y][x] != '.':
            grid[y][x] += 1
        else:
            grid[y][x] = 1
    
    for line in grid:
        string = "".join(str(char) for char in line)
        print(string)

    return True


def part2(fileName: str):
    robots = readFile(fileName)
    seconds = 0
    while True:
        if searchPattern(robots, seconds) == True:
            break
        seconds += 1

    print("Part 2:", seconds)


def main():
    print("Day 14:")
    start_time = time.time()
    part1("input.txt")
    print("--- %s seconds ---" % (time.time() - start_time))

    part2_start_time = time.time()
    part2("input.txt")
    print("--- %s seconds ---" % (time.time() - part2_start_time))


if __name__ == '__main__':
    main()
