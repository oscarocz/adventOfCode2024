import time

# Read puzzle input data
def readFile(fileName: str):
    with open(fileName, "r") as file:
        grid, moves = file.read().split("\n\n")
        grid = [list(line) for line in grid.split()]
        moves = "".join(moves.rstrip().split())
    return grid, moves


def searchRobot(grid: list[list[str]]):
    rows, cols = len(grid), len(grid[0])
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == '@':
                return (row, col)


def pushBox(grid: list[list[str]], boxPos: tuple, dir: tuple):
    ny, nx = boxPos
    while grid[ny][nx] != '#':
        ny += dir[0]
        nx += dir[1]
        if grid[ny][nx] == '.':
            grid[ny][nx] = 'O'
            grid[boxPos[0]][boxPos[1]] = '.'
            return True
    return False

def searchVertLargeBox(grid: list[list[str]], firstBoxPos: list[tuple], dir: tuple):
    verticalBoxes = set()
    verticalBoxes.add(tuple(firstBoxPos))

    # Left Box Part Vertical (Up or Down)
    if grid[firstBoxPos[0][0] + dir[0]][firstBoxPos[0][1]] == ']':
        upRightBoxPart = (firstBoxPos[0][0] + dir[0], firstBoxPos[0][1])
        upLeftBoxPart = (firstBoxPos[0][0] + dir[0], firstBoxPos[0][1] - 1)
        verticalBoxes.update(searchVertLargeBox(grid, [upLeftBoxPart, upRightBoxPart], dir))
    
    # Right Box Part Vertical (Up or Down)
    if grid[firstBoxPos[1][0] + dir[0]][firstBoxPos[1][1]] == '[':
        upRightBoxPart = (firstBoxPos[1][0] + dir[0], firstBoxPos[1][1] + 1)
        upLeftBoxPart = (firstBoxPos[1][0] + dir[0], firstBoxPos[1][1])
        verticalBoxes.update(searchVertLargeBox(grid, [upLeftBoxPart, upRightBoxPart], dir))
    
    # Box has one box in vertical (Up or Down)
    if grid[firstBoxPos[0][0] + dir[0]][firstBoxPos[0][1]] == '[' and grid[firstBoxPos[1][0] + dir[0]][firstBoxPos[1][1]] == ']':
        upRightBoxPart = (firstBoxPos[1][0] + dir[0], firstBoxPos[1][1])
        upLeftBoxPart = (firstBoxPos[0][0] + dir[0], firstBoxPos[0][1])
        verticalBoxes.update(searchVertLargeBox(grid, [upLeftBoxPart, upRightBoxPart], dir))
        # verticalBoxes.add((upLeftBoxPart, upRightBoxPart))
    
    return verticalBoxes


def pushLargeBox(grid: list[list[str]], boxPos: tuple, dir: tuple):
    ny, nx = boxPos

    # Horizontal movement
    if abs(dir[1]) >= 1:
        while grid[ny][nx] != '#':
            nx += dir[1]
            if grid[ny][nx] == '.':
                # Move box horizontally
                for i in range(abs(nx - boxPos[1])):
                    temp = grid[ny][nx]
                    grid[ny][nx] = grid[ny][nx - dir[1]]
                    grid[ny][nx - dir[1]] = temp
                    nx -= dir[1]
                return True
        return False
    # Vertical movement
    else:
        
        largeBoxLeftPos = tuple()
        largeBoxRightPos = tuple()
        if grid[boxPos[0]][boxPos[1]] == '[':
            largeBoxLeftPos = boxPos
            largeBoxRightPos = boxPos[0], boxPos[1] + 1
        else:
            largeBoxLeftPos = boxPos[0], boxPos[1] - 1
            largeBoxRightPos = boxPos

        # Search boxes all boxes needed to move
        boxList = searchVertLargeBox(grid, [largeBoxLeftPos, largeBoxRightPos], dir)

        # Check for Walls
        for box in boxList:
            boxLeftPartCoord = box[0]
            boxRightPartCoord = box[1]
            if grid[boxLeftPartCoord[0] + dir[0]][boxLeftPartCoord[1]] == '#':
                return False
            elif grid[boxRightPartCoord[0] + dir[0]][boxRightPartCoord[1]] == '#':
                return False
            
        # Clear current boxes positions
        for box in boxList:
            boxLeftPartCoord = box[0]
            boxRightPartCoord = box[1]
            grid[boxLeftPartCoord[0]][boxLeftPartCoord[1]] = '.'
            grid[boxRightPartCoord[0]][boxRightPartCoord[1]] = '.'

        # Set new box positions
        for box in boxList:
            boxLeftPartCoord = box[0]
            boxRightPartCoord = box[1]
            grid[boxLeftPartCoord[0] + dir[0]][boxLeftPartCoord[1]] = '['
            grid[boxRightPartCoord[0] + dir[0]][boxRightPartCoord[1]] = ']'

        return True


def moveRobot(grid: list[list[str]], robot_start_pos: tuple, moves: str):
    dirs = {
        "^": (-1, 0),
        'v': (1, 0),
        '<': (0, -1),
        '>': (0, 1)
    }

    robot_pos = robot_start_pos

    for move in moves:
        ny = dirs[move][0] + robot_pos[0]
        nx = dirs[move][1] + robot_pos[1]

        if grid[ny][nx] == '#':
            continue
        elif grid[ny][nx] == '.':
            grid[ny][nx] = '@'
            grid[robot_pos[0]][robot_pos[1]] = '.'
            robot_pos = (ny, nx)
        elif grid[ny][nx] == 'O':
            if pushBox(grid, (ny, nx), dirs[move]):
                grid[ny][nx] = '@'
                grid[robot_pos[0]][robot_pos[1]] = '.'
                robot_pos = (ny, nx)
        else:
            if pushLargeBox(grid, (ny, nx), dirs[move]):
                grid[ny][nx] = '@'
                grid[robot_pos[0]][robot_pos[1]] = '.'
                robot_pos = (ny, nx)


def getBoxPos(grid: list[list[str]]):
    rows, cols = len(grid), len(grid[0])
    boxes = set()
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 'O' or grid[row][col] == '[':
                boxes.add((row, col))
    return boxes


def getGpsCoord(box_pos: set):
    coord = []
    for box in box_pos:
        coord.append(box[0] * 100 + box[1])
    return coord


def scaleMap(grid: list[list[str]]):
    rows, cols = len(grid), len(grid[0])
    scaled_grid = list(list())

    for row in range(rows):
        if row <= len(scaled_grid):
            scaled_grid.append([])
        for col in range(cols):
            if grid[row][col] == '#':
                scaled_grid[row].append('#')
                scaled_grid[row].append('#')
            elif grid[row][col] == '.':
                scaled_grid[row].append('.')
                scaled_grid[row].append('.')
            elif grid[row][col] == 'O':
                scaled_grid[row].append('[')
                scaled_grid[row].append(']')
            elif grid[row][col] == '@':
                scaled_grid[row].append('@')
                scaled_grid[row].append('.')
    return scaled_grid


def part1(fileName: str):
    grid, moves = readFile(fileName)
    robot_pos = searchRobot(grid)
    moveRobot(grid, robot_pos, moves)
    box_pos = getBoxPos(grid)
    gps_coords = getGpsCoord(box_pos)

    # [print(line) for line in grid]

    print("Part 1:", sum(gps_coords))


def part2(fileName: str):
    grid, moves = readFile(fileName)
    grid = scaleMap(grid)
    robot_pos = searchRobot(grid)
    moveRobot(grid, robot_pos, moves)
    box_pos = getBoxPos(grid)
    gps_coords = getGpsCoord(box_pos)

    # [print(line) for line in grid]
    print("Part 2:", sum(gps_coords))


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
