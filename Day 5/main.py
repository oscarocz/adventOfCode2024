
# Read puzzle input
def readFileInput(fileName: str):
    with open(fileName, "r") as file:
        data = [line.rstrip() for line in file]
        separation = data.index("")

        rules = dict()
        for i in data[:separation]:
            key, b = map(int, i.split('|'))
            if key not in rules:
                rules[key] = set()
            rules[key].add(b)
        
        updates = [list(map(int,i.split(','))) for i in data[separation + 1:]]
    return rules, updates

def isCorrect(rules: dict, update:list):
    for i in range(len(update)):
        for j in range(i+1, len(update)):
            if update[i] not in rules:
                return False
            elif update[j] not in rules[update[i]]:
                return False
    return True

def fixUpdate(rules: dict, update:list):
    filteredRules = dict()
    for i in update:
        if i in rules:
            filteredRules[i] = set(update) & rules[i]
    orderedUpdate = sorted(filteredRules, key=lambda k: len(filteredRules[k]), reverse=True)
    # print(filteredRules)
    print(orderedUpdate)
    return orderedUpdate

def part1(fileName: str):
    rules, updates = readFileInput(fileName)
    addUp = 0

    for update in updates:
        if isCorrect(rules, update):
            addUp += update[len(update) // 2]

    print(addUp)

def part2(fileName: str):
    rules, updates = readFileInput(fileName)
    addUp = 0
    for update in updates:
        if not isCorrect(rules, update):
            fixedUpdate = fixUpdate(rules, update)
            addUp += fixedUpdate[len(update) // 2]
    print(addUp)

# Day 5
def main():
    print("Day 5:")
    part1("input.txt")
    part2("input.txt")


if __name__ == '__main__':
    main()