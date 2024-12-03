import re

# Read puzzle input data
def readFileInput(file: str):
    with open(file, "r") as input:
        data = input.read()
    return data

# Day 3 Part 1
def part1(file: str):
    data = readFileInput(file)
    # Find & extract mul(xyz,xyz) pattern
    instructionList = re.findall(r'mul\(\d{1,3},\d{1,3}\)', data)
    # Extract data in a list
    multList = [list(map(int, re.findall(r'\d+', i))) for i in instructionList]
    # Compute result
    resultList = [mult[1] * mult[0] for mult in multList]
    result = sum(resultList)

    print("Part 1 Result:", result)

# Day 3 Part 2
def part2(file: str):
    data = readFileInput(file)
    # Execute Do() & Don't() instructions and filters the instruction list
    filteredInput = re.sub(r"don't\(\).*?do\(\)", '', data, flags=re.DOTALL)
    # Find & extract mul(xyz,xyz) pattern
    instructionList = re.findall(r'mul\(\d{1,3},\d{1,3}\)', filteredInput)
    # Extract data in a list
    multList = [list(map(int, re.findall(r'\d+', i))) for i in instructionList]
    # Compute result
    resultList = [mult[1] * mult[0] for mult in multList]
    result = sum(resultList)

    print("Part 2 Result:", result)


def main():
    print("Day 3:")
    part1("input.txt")
    part2("input.txt")


if __name__ == '__main__':
    main()
