from intcode_computer import intcode_computer

with open("input/day09.txt") as file:
    input = file.read()


def part1():
    intcode_computer(input).run(1)


def part2():
    intcode_computer(input).run(2)


part1()
part2()
