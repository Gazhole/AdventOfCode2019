"""
Advent of Code 2019
Day 5
"""


def increment_i(opcode, out_pos, i):
    pos_jumps = dict()
    pos_jumps[1] = 4
    pos_jumps[2] = 4
    pos_jumps[3] = 2
    pos_jumps[4] = 2
    pos_jumps[5] = 4
    pos_jumps[6] = 4
    pos_jumps[7] = 4
    pos_jumps[8] = 4
    pos_jumps[99] = 0

    if out_pos == i:
        return 0
    else:
        return pos_jumps[opcode]


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


def opcode_1(opcode, program, i, param_1_mode, param_2_mode, param_3_mode):
    in_1_value = get_input_param(program, 1, i, param_1_mode)
    in_2_value = get_input_param(program, 2, i, param_2_mode)
    out_pos = get_output_pos(program, 3, i, param_3_mode)

    program[out_pos] = int(in_1_value) + int(in_2_value)

    return increment_i(opcode, out_pos, i)


def opcode_2(opcode, program, i, param_1_mode, param_2_mode, param_3_mode):
    in_1_value = get_input_param(program, 1, i, param_1_mode)
    in_2_value = get_input_param(program, 2, i, param_2_mode)
    out_pos = get_output_pos(program, 3, i, param_3_mode)

    program[out_pos] = int(in_1_value) * int(in_2_value)

    return increment_i(opcode, out_pos, i)


def opcode_3(opcode, program, i, param_1_mode, param_2_mode, param_3_mode):
    out_pos = get_output_pos(program, 1, i, param_1_mode)
    in_1_value = input(">")

    program[out_pos] = in_1_value

    return increment_i(opcode, out_pos, i)


def opcode_4(opcode, program, i, param_1_mode, param_2_mode, param_3_mode):
    print(program[program[i + 1]])

    return increment_i(opcode, False, i)


def opcode_5(opcode, program, i, param_1_mode, param_2_mode, param_3_mode):
    in_1_value = get_input_param(program, 1, i, param_1_mode)
    in_2_value = get_input_param(program, 2, i, param_2_mode)

    if in_1_value != 0:
        pos_jump = in_2_value - i
        return pos_jump
    else:
        return 3


def opcode_6(opcode, program, i, param_1_mode, param_2_mode, param_3_mode):
    in_1_value = get_input_param(program, 1, i, param_1_mode)
    in_2_value = get_input_param(program, 2, i, param_2_mode)

    if in_1_value == 0:
        pos_jump = in_2_value - i
        return pos_jump
    else:
        return 3


def opcode_7(opcode, program, i, param_1_mode, param_2_mode, param_3_mode):
    in_1_value = get_input_param(program, 1, i, param_1_mode)
    in_2_value = get_input_param(program, 2, i, param_2_mode)
    out_pos = get_output_pos(program, 3, i, param_3_mode)

    if in_1_value < in_2_value:
        program[out_pos] = 1
    else:
        program[out_pos] = 0

    return increment_i(opcode, out_pos, i)


def opcode_8(opcode, program, i, param_1_mode, param_2_mode, param_3_mode):
    in_1_value = get_input_param(program, 1, i, param_1_mode)
    in_2_value = get_input_param(program, 2, i, param_2_mode)
    out_pos = get_output_pos(program, 3, i, param_3_mode)

    if in_1_value == in_2_value:
        program[out_pos] = 1
    else:
        program[out_pos] = 0

    return increment_i(opcode, out_pos, i)


def opcode_99(opcode, program, i, param_1_mode, param_2_mode, param_3_mode):
    print(program)

    return increment_i(opcode, False, i)


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
    opcodes[5] = opcode_5
    opcodes[6] = opcode_6
    opcodes[7] = opcode_7
    opcodes[8] = opcode_8
    opcodes[99] = opcode_99

    i = 0
    while True:
        opcode, param_1_mode, param_2_mode, param_3_mode = parse_opcode(program[i])

        f = opcodes[opcode]
        pos_jump = f(opcode, program, i, param_1_mode, param_2_mode, param_3_mode)

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
