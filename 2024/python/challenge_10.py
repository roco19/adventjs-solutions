from time import sleep
from typing import List

# fmt: off
instructions_1 = [
  "MOV -1 C",
  "INC C",
  "JMP C 1",
  "MOV C A",
  "INC A"
]

instructions_2 = [
  "MOV 5 B",
  "DEC B",
  "MOV B A",
  "INC A"
]
# fmt: on


def compile(instructions: List[str]):
    registers = {}

    def get_value(x):
        try:
            return int(x)
        except ValueError:
            return registers.get(x, 0)

    index = 0
    while index < len(instructions):
        instruction_parts = instructions[index].split()
        instruction = instruction_parts[0]

        if instruction == "MOV":
            registers[instruction_parts[2]] = get_value(instruction_parts[1])

        elif instruction == "INC":
            register = instruction_parts[1]
            registers[register] = registers.get(register, 0) + 1

        elif instruction == "DEC":
            register = instruction_parts[1]
            registers[register] = registers.get(register, 0) - 1

        elif instruction == "JMP":
            if registers.get(instruction_parts[1], 0) == 0:
                index = int(instruction_parts[2])
                continue

        index += 1

    return registers.get("A", "undefined")


if __name__ == "__main__":
    print(compile(instructions_2))
