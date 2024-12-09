import re

with open("input.txt", "r") as file:
    input = file.read()

def part1(puzzle_input):
    total = 0
    for a, b in re.findall(r"mul\((\d+),(\d+)\)", puzzle_input):
        total += int(a) * int(b)
        
    return total

def part2(puzzle_input):
    do = r"do\(\)"
    dont = r"don't\(\)"
    mul = r"mul\((\d+),(\d+)\)"
    total = 0
    enabled = True
    for x in re.finditer(f'{do}|{dont}|{mul}', puzzle_input):
        if re.fullmatch(do, x.group()):
            enabled = True
        elif re.fullmatch(dont, x.group()):
            enabled = False
        elif enabled:
            total += int(x.group(1)) * int(x.group(2))

    return total


total = part2(input)
print(total)