from intcode_computer import intcode_computer

with open("input/day05.txt") as file:
    input = file.read()


def part1():
    return intcode_computer(input).run(1)


def part2():
    return intcode_computer(input).run(5)


part1()
part2()
