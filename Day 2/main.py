
# Read puzzle input data
def readFileInput(file: str):
    with open(file, "r") as data:
        lines = data.read().splitlines()
    reportList = []
    for line in lines:
        reportList.append(list(map(int, line.split())))
    return reportList

# Check report safety from levels
def checkReportSafety(reportLevel: list):
    safe = True
    if reportLevel[1] > reportLevel[0]:
        for i in range(1, len(reportLevel)):
            diff = reportLevel[i] - reportLevel[i-1]
            if diff <= 0 or diff > 3:
                safe = False
                break
    elif reportLevel[1] < reportLevel[0]:
        for i in range(1, len(reportLevel)):
            diff = reportLevel[i] - reportLevel[i-1]
            if diff >= 0 or diff < -3:
                safe = False
                break
    else:
        safe = False

    return safe

# Day 2 Part 1 Solution
def part1(file: str):
    reportList = readFileInput(file)
    nSafeReports = len(reportList)

    for report in reportList:
        safety = checkReportSafety(report)
        if safety != True:
            nSafeReports = nSafeReports - 1

    print("Part 1 Result:", nSafeReports)

# Day 2 Part 2 Solution
def part2(file: str):
    reportList = readFileInput(file)
    nSafeReports = 0

    for report in reportList:
        safety = checkReportSafety(report)
        if safety == True:
            nSafeReports = nSafeReports + 1
        else:
            for i in range(len(report)):
                copyReport = report.copy()
                copyReport.pop(i)
                safety = checkReportSafety(copyReport)
                if safety == True:
                    nSafeReports = nSafeReports + 1
                    break

    print("Part 2 Result:", nSafeReports)


def main():
    print("Day 2:")
    part1("input.txt")
    part2("input.txt")


if __name__ == '__main__':
    main()
