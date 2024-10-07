import re


class intcode_computer:

    instruction_pattern = re.compile(r"(\d)(\d)(\d)(\d{2})")

    opcode_map = {
        1: "add",
        2: "multiply",
        3: "input",
        4: "output",
        5: "jump-if-true",
        6: "jump-if-false",
        7: "less than",
        8: "equals",
        9: "relative-base-offset",
        99: "exit",
    }

    def __init__(self, input, return_first_output=False):
        self.memory = [int(x) for x in input.split(",")]
        self.memory.extend([0 for _ in range(10_000 - len(self.memory))])
        self.pointer = 0
        self.relative_base = 0
        self.return_first_output = return_first_output

    def get_param_value(self, mode_param, param):
        if mode_param == "0":
            return self.memory[param]
        elif mode_param == "1":
            return param
        elif mode_param == "2":
            return self.memory[param + self.relative_base]

    def get_param_address(self, mode_param, param):
        if mode_param == "0":
            return param
        elif mode_param == "2":
            return param + self.relative_base

    def run(self, *input_values):
        input_values_index = 0
        while True:
            instruction = str(self.memory[self.pointer]).rjust(5, "0")
            m = self.instruction_pattern.match(instruction)
            opcode = m.group(4)
            mode_param1 = m.group(3)
            mode_param2 = m.group(2)
            mode_param3 = m.group(1)
            function = self.opcode_map.get(int(opcode))

            if function == "exit":
                break

            # Param definition
            param1 = self.memory[self.pointer + 1]
            self.pointer += 2
            param1_value = self.get_param_value(mode_param1, param1)
            param1_address = self.get_param_address(mode_param1, param1)

            if function not in ("input", "output", "relative-base-offset"):
                param2 = self.memory[self.pointer]
                self.pointer += 1
                param2_value = self.get_param_value(mode_param2, param2)

                if function not in ("jump-if-true", "jump-if-false"):
                    param3 = self.memory[self.pointer]
                    self.pointer += 1
                    param3_address = self.get_param_address(mode_param3, param3)

            # Function processing
            if function == "add":
                self.memory[param3_address] = param1_value + param2_value

            elif function == "multiply":
                self.memory[param3_address] = param1_value * param2_value

            elif function == "less than":
                self.memory[param3_address] = 1 if param1_value < param2_value else 0

            elif function == "equals":
                self.memory[param3_address] = 1 if param1_value == param2_value else 0

            elif function == "jump-if-true":
                if param1_value != 0:
                    self.pointer = param2_value

            elif function == "jump-if-false":
                if param1_value == 0:
                    self.pointer = param2_value

            elif function == "input":
                self.memory[param1_address] = input_values[input_values_index]
                input_values_index += 1

            elif function == "output":
                if self.return_first_output:
                    return param1_value
                print(param1_value)

            elif function == "relative-base-offset":
                self.relative_base += param1_value
