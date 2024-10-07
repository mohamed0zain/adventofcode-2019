import collections


def is_valid_part1(password):
    return password == "".join(sorted(password)) and len(set(password)) < 6


def is_valid_part2(password):
    return password == "".join(sorted(password)) and 2 in collections.Counter(password).values()


def exec():
    part1 = 0
    part2 = 0

    for i in range(172851, 675869 + 1):
        if is_valid_part1(str(i)):
            part1 += 1
        if is_valid_part2(str(i)):
            part2 += 1

    print(part1)
    print(part2)


exec()
