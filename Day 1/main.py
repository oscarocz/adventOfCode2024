
# Read puzzle input data
def readFileInput(file: str):
    with open(file, "r") as data:
        list1 = []
        list2 = []
        for line in data:
            p = line.split()
            list1.append(int(p[0]))
            list2.append(int(p[1]))

    return list1, list2

# Day 1 Part 1 Solution
def part1(file: str):
    list1, list2 = readFileInput(file)
    list1.sort()
    list2.sort()
    listDiff = [abs(list1_i - list2_i)
                for list1_i, list2_i in zip(list1, list2)]
    totalDiff = sum(listDiff)
    print("Part 1 Result:", totalDiff)

# Day 1 Part 2 Solution
def part2(file: str):
    list1, list2 = readFileInput(file)
    similScoreList = []
    for data in list1:
        similScoreList.append(data * list2.count(data))
    similScore = sum(similScoreList)
    print("Part 2 Result:", similScore)


def main():
    print("Day 1:")
    part1("input.txt")
    part2("input.txt")


if __name__ == '__main__':
    main()
