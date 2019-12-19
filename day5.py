"""
Advent of Code 2019
Day 5
"""


def get_input_param(program, param_num, i, mode):
    if mode == 0:
        value = program[program[i + param_num]]
    elif mode == 1:
        value = program[i + param_num]

    return value


def get_output_pos(program, param_num, i, mode):
    if mode == 0:
        pos = program[i + param_num]
    elif mode == 1:
        pos = program[program[i + param_num]]

    return pos


def opcode_1(program, i, param_1_mode, param_2_mode, param_3_mode):

    in_1_value = get_input_param(program, 1, i, param_1_mode)
    in_2_value = get_input_param(program, 2, i, param_2_mode)
    out_pos = get_output_pos(program, 3, i, param_3_mode)

    program[out_pos] = int(in_1_value) + int(in_2_value)

    return 4


def opcode_2(program, i, param_1_mode, param_2_mode, param_3_mode):

    in_1_value = get_input_param(program, 1, i, param_1_mode)
    in_2_value = get_input_param(program, 2, i, param_2_mode)
    out_pos = get_output_pos(program, 3, i, param_3_mode)

    program[out_pos] = int(in_1_value) * int(in_2_value)

    return 4


def opcode_3(program, i, param_1_mode, param_2_mode, param_3_mode):
    out_pos = get_output_pos(program, 1, i, param_1_mode)
    in_1_value = input(">")

    program[out_pos] = in_1_value

    return 2


def opcode_4(program, i, param_1_mode, param_2_mode, param_3_mode):
    print(program[program[i + 1]])

    return 2


def opcode_5(program, i, param_1_mode, param_2_mode, param_3_mode):
    in_1_value = get_input_param(program, 1, i, param_1_mode)
    in_2_value = get_input_param(program, 2, i, param_2_mode)

    if in_1_value != 0:
        pos_jump = in_2_value - i
        return pos_jump
    else:
        return 0


def opcode_6(program, i, param_1_mode, param_2_mode, param_3_mode):
    in_1_value = get_input_param(program, 1, i, param_1_mode)
    in_2_value = get_input_param(program, 2, i, param_2_mode)

    if in_1_value == 0:
        pos_jump = in_2_value - i
        return pos_jump
    else:
        return 0


def opcode_7(program, i, param_1_mode, param_2_mode, param_3_mode):
    pass


def opcode_8(program, i, param_1_mode, param_2_mode, param_3_mode):
    pass


def opcode_99(program, i, param_1_mode, param_2_mode, param_3_mode):
    print(program)

    return 0


def parse_opcode(opcode):
    opcode = str(opcode)

    for i in range(5 - len(opcode)):
        opcode = "0" + opcode

    e = int(opcode[-1])
    d = int(opcode[-2])
    c = int(opcode[-3])
    b = int(opcode[-4])
    a = int(opcode[-5])

    opcode = int(str(d) + str(e))
    param_1_mode = c
    param_2_mode = b
    param_3_mode = a

    return opcode, param_1_mode, param_2_mode, param_3_mode


def parse_program(program):
    opcodes = dict()
    opcodes[1] = opcode_1
    opcodes[2] = opcode_2
    opcodes[3] = opcode_3
    opcodes[4] = opcode_4
    opcodes[99] = opcode_99

    i = 0
    while True:
        opcode, param_1_mode, param_2_mode, param_3_mode = parse_opcode(program[i])

        f = opcodes[opcode]
        pos_jump = f(program, i, param_1_mode, param_2_mode, param_3_mode)

        if program[i] == 99:
            break
        else:
            i += pos_jump


def main():

    with open("day5input.txt", "r") as input_file:
        program_raw = [line.split(",") for line in input_file]
        program = [int(segment) for segment in program_raw[0]]

    parse_program(program)


if __name__ == "__main__":
    main()
