import copy

# Read puzzle input data
def readFile(fileName: str):
    with open(fileName, "r") as file:
        data = list(map(int,list(file.read().strip())))
    return data

def parseDiskMap(diskMap: list[int]):
    diskSize = len(diskMap)
    diskData = list()

    for i in range(0, diskSize, 2):
        if (i+1 >= diskSize):
            diskData.append([diskMap[i], 0])
        else:
            diskData.append([diskMap[i], diskMap[i+1]])
    
    print(diskData)


def decodeDiskMap(diskMap: list[int]):
    diskMapLen = len(diskMap)
    rawData = list()

    for i in range(diskMapLen):
        if i % 2 == 0:
            # ID
            data = i // 2 
        else:
            data = '.'

        for j in range(diskMap[i]):
            rawData.append(data)
    return rawData

def fileCompact(rawData: list):
    lastIndex = len(rawData) - 1
    firstIndex = 0

    while (firstIndex < lastIndex):
        if rawData[lastIndex] != '.':
            for j in range(firstIndex, lastIndex + 1):
                if rawData[j] == '.':
                    rawData[j] = rawData[lastIndex]
                    rawData[lastIndex] = '.'
                    firstIndex = j
                    break
        lastIndex -= 1

def searchAndFillBlock(rawData: list, id: int, blockSize: int, limitIdx: int):
    freeBlockCount = 0
    try:
        firstFreeSpace = rawData.index('.')
    except:
        return False
    
    for i in range(firstFreeSpace,len(rawData)):
        if i >= limitIdx:
            return False
        if rawData[i] == '.':
            freeBlockCount += 1
        else:
            freeBlockCount = 0

        if freeBlockCount >= blockSize:
            for j in range(i,i - freeBlockCount,-1):
                rawData[j] = id
                freeBlockCount = 0
            break

    if freeBlockCount != 0:
        return False
    
    
    return True

def fileCompactBlock(rawData: list):
    id = -1
    blockCount = 0
    rawDataCopy = copy.deepcopy(rawData)

    for idx, data in enumerate(reversed(rawDataCopy)):
        if id == data:
            blockCount += 1
        elif blockCount != 0:
            if (searchAndFillBlock(rawData, id, blockCount, len(rawData)-idx) == True):
                for i in range(-idx+blockCount-1, -idx-1, -1):
                    rawData[i] = '.'
            if data != '.':
                blockCount = 1
                id = data
            else:
                blockCount = 0
        elif data != '.':
            blockCount += 1
            id = data


def checksum(rawData: list):
    chk = 0
    for i in range(len(rawData)):
        if type(rawData[i]) is int:
            chk += i * rawData[i]
    return chk


def part1(fileName: str):

    data = readFile(fileName)
    rawData = decodeDiskMap(data)
    # print(rawData)
    fileCompact(rawData)
    # print(rawData[:rawData.index('.')])
    result = checksum(rawData[:rawData.index('.')])
    print("Part 1",result)

def part2(fileName: str):
    data = readFile(fileName)
    rawData = decodeDiskMap(data)
    print(rawData)
    fileCompactBlock(rawData)
    result = checksum(rawData)
    print("Part 2",result)

def main():
    print("Day 9:")
    part1("input.txt")
    part2("input.txt")


if __name__ == '__main__':
    main()