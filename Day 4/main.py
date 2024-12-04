
# Read puzzle input data
def readFileInput(file: str):
    with open(file, "r") as file:
        data = [line.rstrip() for line in file]
    return data


def searchHorizontal(data: list, word: str):
    reversedWord = word[::-1]
    count = 0

    for line in data:
        count += line.count(word)
        count += line.count(reversedWord)

    return count


def searchVertical(data: list, word: str):
    verticalList = [''.join(idx) for idx in zip(*data)]
    reversedWord = word[::-1]
    count = 0

    for line in verticalList:
        count += line.count(word)
        count += line.count(reversedWord)

    return count


def searchDiagonal(grid: list, word: str):
    rows, cols = len(grid), len(grid[0])
    diagonal = {}
    antidiagonal = {}
    reversedWord = word[::-1]
    count = 0

    for r in range(rows):
        for c in range(cols):
            keyDiag = r - c
            if keyDiag not in diagonal:
                diagonal[keyDiag] = ""
            diagonal[keyDiag] += (grid[r][c])

            keyAntidiag = r + c
            if keyAntidiag not in antidiagonal:
                antidiagonal[keyAntidiag] = ""
            antidiagonal[keyAntidiag] += grid[r][c]

    for line in diagonal.values():
        count += line.count(word)
        count += line.count(reversedWord)

    for line in antidiagonal.values():
        count += line.count(word)
        count += line.count(reversedWord)

    return count

# Day 4 Part 1
def part1(file: str):
    data = readFileInput(file)
    count = searchHorizontal(data, 'XMAS')
    count += searchVertical(data, 'XMAS')
    count += searchDiagonal(data, 'XMAS')
    print("Part 1 Result:", count)

# Day 4 Part 2:
def part2(file: str):
    grid = readFileInput(file)
    count = 0

    for row in range(1, len(grid)-1):
        for col in range(1, len(grid[row])-1):
            if grid[row][col] == 'A':
                if {grid[row-1][col-1], grid[row+1][col+1]} == {'M', 'S'} and {grid[row-1][col+1], grid[row+1][col-1]} == {'M', 'S'}:
                    count += 1

    print("Part 2 Result:", count)


def main():
    print("Day 4:")
    part1("input.txt")
    part2("input.txt")


if __name__ == '__main__':
    main()
