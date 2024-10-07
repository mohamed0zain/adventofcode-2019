with open("input/day02.txt") as file:
    input = file.read()


def run(noun, verb):
    memory = [int(x) for x in input.split(",")]
    memory[1] = noun
    memory[2] = verb

    pointer = 0
    instruction = 0
    while instruction != 99:
        instruction = memory[pointer]
        param1 = memory[pointer + 1]
        param2 = memory[pointer + 2]
        param3 = memory[pointer + 3]
        pointer += 4

        if instruction == 1:
            memory[param3] = memory[param1] + memory[param2]
        elif instruction == 2:
            memory[param3] = memory[param1] * memory[param2]

    return memory[0]


def part1():
    return run(12, 2)


def part2():
    for noun in range(100):
        for verb in range(100):
            if run(noun, verb) == 19690720:
                return 100 * noun + verb


print(part1())
print(part2())
