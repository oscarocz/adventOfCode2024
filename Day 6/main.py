import copy

# Read puzzle input
def readFileInput(fileName: str):
    with open(fileName, "r") as file:
        data = [list(line.rstrip()) for line in file]
    return data

def searchGuard(map: list[list[str]]):
    for idy in range(len(map)):
        for idx in range(len(map[idy])):
            if map[idy][idx] == '^':
                return idx, idy

def patrolUp(map:list, idx:int, idy: int):
    for idy in range(idy, -1, -1):
        if map[idy][idx] == '#' or map[idy][idx] == 'O':
            return True, idx, idy+1
        map[idy][idx] = 'X'
    return False, idx, idy

def patrolDown(map:list, idx:int, idy: int):
    for idy in range(idy, len(map)):
        if map[idy][idx] == '#' or map[idy][idx] == 'O':
            return True, idx, idy-1
        map[idy][idx] = 'X'
    return False, idx, idy

def patrolRight(map:list, idx:int, idy: int):
    for idx in range(idx, len(map[idy])):
        if map[idy][idx] == '#' or map[idy][idx] == 'O':
            return True, idx-1, idy
        map[idy][idx] = 'X'
    return False, idx, idy

def patrolLeft(map:list, idx:int, idy: int):
    for idx in range(idx, -1, -1):
        if map[idy][idx] == '#' or map[idy][idx] == 'O':
            return True, idx+1, idy
        map[idy][idx] = 'X'
    return False, idx, idy

# Set patrol positions in map
def setPatrolMap(map: list, startIdx:int, startIdy: int):
    idx = startIdx
    idy = startIdy
    while(True):
        patrolInMap, idx, idy = patrolUp(map, idx, idy)
        if patrolInMap == False:
            return
        patrolInMap, idx, idy = patrolRight(map, idx, idy)
        if patrolInMap == False:
            return
        patrolInMap, idx, idy = patrolDown(map, idx, idy)
        if patrolInMap == False:
            return
        patrolInMap, idx, idy = patrolLeft(map, idx, idy)
        if patrolInMap == False:
            return

# Count number of patrol positions in map
def countPatrolPos(map: list) -> int:
    return sum([(''.join(map[idy])).count('X') for idy in range(len(map))])

# Get patrol positions in map
def getPatrolPos(map: list[list[str]]) -> set:
    patrolPos = set()
    for idy in range(0, len(map)):
        for idx in range(0, len(map[idy])):
            if map[idy][idx] == 'X':
                patrolPos.add(tuple([idx,idy]))
    return patrolPos

# Check if patrol is in loop
def isPatrolLoop(map: list, startIdx:int, startIdy: int):
    idx = startIdx
    idy = startIdy
    lastPatrolPos = list()
    while(True):
        patrolInMap, idx, idy = patrolUp(map, idx, idy)
        lastPatrolPos.append([idx,idy])
        if patrolInMap == False:
            return False
        patrolInMap, idx, idy = patrolRight(map, idx, idy)
        lastPatrolPos.append([idx,idy])
        if patrolInMap == False:
            return False
        patrolInMap, idx, idy = patrolDown(map, idx, idy)
        lastPatrolPos.append([idx,idy])
        if patrolInMap == False:
            return False
        patrolInMap, idx, idy = patrolLeft(map, idx, idy)
        lastPatrolPos.append([idx,idy])
        if patrolInMap == False:
            return False
        
        if lastPatrolPos.count([idx,idy]) > 2:
            return True


def part1(fileName: str):
    map = readFileInput(fileName)

    # print("Original Map")
    # [print(''.join(map[idy])) for idy in range(len(map))]

    x, y = searchGuard(map)
    setPatrolMap(map, x, y)
    count = countPatrolPos(map)

    # print("New Map:")
    # [print(''.join(map[idy])) for idy in range(len(map))]
    print("Part 1 Result:", count)

def part2(fileName: str):
    map = readFileInput(fileName)
    x, y = searchGuard(map)

    patrolMap = copy.deepcopy(map)
    setPatrolMap(patrolMap, x, y)
    patrolPos = getPatrolPos(patrolMap)

    # Erase initial patrol position
    patrolPos.remove(tuple([x,y]))

    loopCount = 0
    for pos in patrolPos:
        obstructedMap = copy.deepcopy(map)
        obstructedMap[pos[1]][pos[0]] = 'O'
        if isPatrolLoop(obstructedMap, x, y):
            loopCount += 1
            # print(pos,"\n")
            # [print(''.join(obstructedMap[idy])) for idy in range(len(obstructedMap))]

    print("Part 2 Result:", loopCount)

# Day 6
def main():
    print("Day 6:")
    part1("input.txt")
    part2("input.txt")


if __name__ == '__main__':
    main()