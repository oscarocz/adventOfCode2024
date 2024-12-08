# Read puzzle input
def readFileInput(fileName: str):
    with open(fileName, "r") as file:
        equations = list()
        for line in file:
            testValue, operands = line.split(':')
            equations.append((int(testValue), [*map(int,operands.strip().split())]))
    return equations

def part1(fileName: str):
    equations = readFileInput(fileName)
    result = 0
    for testValue, operands in equations:
        possibilities = [operands.pop(0)]
        for operand in operands:
            countUpPossibility = len(possibilities)
            # Inverted copy of possibilities (+,x) -> (+,x,x,+)...
            [possibilities.append(possibilities[i]) for i in range(countUpPossibility-1,-1,-1)]
            # Obtain possibilities result (++,xx,x+,+x)...
            for i in range(0,len(possibilities),2):
                possibilities[i] += operand
                possibilities[i+1] *= operand
        if testValue in possibilities:
            result += testValue

    print(result)

def part2(fileName: str):
    equations = readFileInput(fileName)
    result = 0
    for testValue, operands in equations:
        possibilities = [operands.pop(0)]
        for operand in operands:
            temp = list()
            for p in possibilities:
                nextValues = [
                        p + operand,
                        p * operand,
                        int(str(p) + str(operand)),
                ]
                temp.extend([v for v in nextValues if v <= testValue])
            possibilities = temp

        if testValue in possibilities:
            result += testValue
    print(result)

# Day 7
def main():
    print("Day 7:")
    part1("input.txt")
    part2("input.txt")


if __name__ == '__main__':
    main()
