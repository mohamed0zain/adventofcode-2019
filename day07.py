from intcode_computer import intcode_computer

with open("input/day07.txt") as file:
    input = file.read()


def part1():
    values = []

    for amp_a_setting in range(5):
        for amp_b_setting in range(5):
            for amp_c_setting in range(5):
                for amp_d_setting in range(5):
                    for amp_e_setting in range(5):
                        if len({amp_a_setting, amp_b_setting, amp_c_setting, amp_d_setting, amp_e_setting,}) != 5:
                            continue

                        amp_a_output = intcode_computer(input, True).run(amp_a_setting, 0)
                        amp_b_output = intcode_computer(input, True).run(amp_b_setting, amp_a_output)
                        amp_c_output = intcode_computer(input, True).run(amp_c_setting, amp_b_output)
                        amp_d_output = intcode_computer(input, True).run(amp_d_setting, amp_c_output)
                        amp_e_output = intcode_computer(input, True).run(amp_e_setting, amp_d_output)

                        values.append(amp_e_output)

    return max(values)


def part2():
    values = []

    for amp_a_setting in range(5, 10):
        for amp_b_setting in range(5, 10):
            for amp_c_setting in range(5, 10):
                for amp_d_setting in range(5, 10):
                    for amp_e_setting in range(5, 10):
                        if len({amp_a_setting, amp_b_setting, amp_c_setting, amp_d_setting, amp_e_setting,}) != 5:
                            continue

                        amp_a_computer = intcode_computer(input, True)
                        amp_b_computer = intcode_computer(input, True)
                        amp_c_computer = intcode_computer(input, True)
                        amp_d_computer = intcode_computer(input, True)
                        amp_e_computer = intcode_computer(input, True)

                        amp_a_output = amp_a_computer.run(amp_a_setting, 0)
                        amp_b_output = amp_b_computer.run(amp_b_setting, amp_a_output)
                        amp_c_output = amp_c_computer.run(amp_c_setting, amp_b_output)
                        amp_d_output = amp_d_computer.run(amp_d_setting, amp_c_output)
                        amp_e_output = amp_e_computer.run(amp_e_setting, amp_d_output)

                        last_value = 0

                        while True:
                            amp_a_output = amp_a_computer.run(amp_e_output)
                            amp_b_output = amp_b_computer.run(amp_a_output)
                            amp_c_output = amp_c_computer.run(amp_b_output)
                            amp_d_output = amp_d_computer.run(amp_c_output)
                            amp_e_output = amp_e_computer.run(amp_d_output)

                            if amp_e_output is None:
                                break

                            last_value = amp_e_output

                        values.append(last_value)

    return max(values)


print(part1())
print(part2())
