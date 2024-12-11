import time
from collections import defaultdict
from math import log10, floor

# Read puzzle input data
def readFile(fileName: str):
    with open(fileName, "r") as file:
        data = list(map(int, file.read().split()))
    return data


def blink(rocks: dict[int]):

    oldRocks = rocks.copy()
    
    for keyValue in oldRocks:
        count = oldRocks[keyValue]
        if keyValue == 0:
            rocks[1] += count
        elif (digits := floor(log10(keyValue) + 1)) % 2 == 0:
            rocks[keyValue // (10 ** (digits // 2))] += count
            rocks[keyValue % (10 ** (digits // 2))] += count
        else:
            rocks[keyValue * 2024] += count
        
        currentCount =  rocks[keyValue] - count
        if currentCount > 0:
            rocks[keyValue] -= count
        else:
            del rocks[keyValue]
    
    rocks = oldRocks.copy()


def part1(fileName: str):

    data = readFile(fileName)
    rocks = defaultdict(int)
    for i in data:
        rocks[i] += 1

    for i in range(25):
        blink(rocks)
    print("Part 1:", sum(rocks.values()))


def part2(fileName: str):

    data = readFile(fileName)
    rocks = defaultdict(int)
    for i in data:
        rocks[i] += 1

    for i in range(75):
        blink(rocks)

    print("Part 2:", sum(rocks.values()))



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
