import time

# Read puzzle input data
def readFile(fileName: str):
    with open(fileName, "r") as file:
        data = file.read().split("\n\n")
    return data


def part1(fileName: str):
    machines = readFile(fileName)

    tokens = 0
    for machine in machines:
        button_A, button_B, prize = machine.split("\n")
        button_A = [
            *map(lambda i: int(i[2:]), button_A.split(": ")[1].split(", "))]
        button_B = [
            *map(lambda i: int(i[2:]), button_B.split(": ")[1].split(", "))]
        prize = [*map(lambda i: int(i[2:]), prize.split(": ")[1].split(", "))]

        times_A = (prize[1] * button_B[0] - prize[0] * button_B[1]) / \
            (button_A[1] * button_B[0] - button_B[1] * button_A[0])
        times_B = (prize[1] - times_A * button_A[1]) / button_B[1]

        if times_A.is_integer() and times_B.is_integer() and int(times_A) <= 100 and int(times_B) <= 100:
            tokens += int(times_A) * 3 + int(times_B)

    print("Part 1:", tokens)


def part2(fileName: str):
    machines = readFile(fileName)

    tokens = 0
    for machine in machines:
        button_A, button_B, prize = machine.split("\n")
        button_A = [
            *map(lambda i: int(i[2:]), button_A.split(": ")[1].split(", "))]
        button_B = [
            *map(lambda i: int(i[2:]), button_B.split(": ")[1].split(", "))]
        prize = [*map(lambda i: int(i[2:]) + 10000000000000, prize.split(": ")[1].split(", "))]

        times_A = (prize[1] * button_B[0] - prize[0] * button_B[1]) / \
            (button_A[1] * button_B[0] - button_B[1] * button_A[0])
        times_B = (prize[1] - times_A * button_A[1]) / button_B[1]

        if times_A.is_integer() and times_B.is_integer():
            tokens += int(times_A) * 3 + int(times_B)

    print("Part 2:", tokens)


def main():
    print("Day 13:")
    start_time = time.time()
    part1("input.txt")
    print("--- %s seconds ---" % (time.time() - start_time))

    part2_start_time = time.time()
    part2("input.txt")
    print("--- %s seconds ---" % (time.time() - part2_start_time))


if __name__ == '__main__':
    main()
