with open("input/day01.txt") as file:
    input = file.read().splitlines()


def calculate_fuel(mass):
    return int(mass / 3) - 2


def part1():
    total = 0

    for module_mass in input:
        total += calculate_fuel(int(module_mass))

    return total


def part2():
    total = 0

    for module_mass in input:
        fuel = int(module_mass)

        while fuel >= 9:
            fuel = calculate_fuel(fuel)
            total += fuel

    return total


print(part1())
print(part2())
