"""
Advent of Code 2019
Day 2
"""


def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


def terminate(program):
    return program


def lookup_value(program, position):
    return program[program[position]]


def run_program(program):
    op_codes = dict()
    op_codes[1] = add
    op_codes[2] = multiply
    op_codes[99] = terminate

    oc_positions = range(0, len(program), 4)

    for pos in oc_positions:
        if program[pos] == 99:
            print(program)
        else:
            op_code = program[pos]
            try:
                result_position = program[pos + 3]
            except IndexError:
                continue
            a_input = lookup_value(program, pos + 1)
            b_input = lookup_value(program, pos + 2)

            program[result_position] = op_codes[op_code](a_input, b_input)


def main():
    # run_program([1,12,2,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,6,19,23,1,23,13,27,2,6,27,31,1,5,31,35,2,10,35,39,1,6,39,43,1,13,43,47,2,47,6,51,1,51,5,55,1,55,6,59,2,59,10,63,1,63,6,67,2,67,10,71,1,71,9,75,2,75,10,79,1,79,5,83,2,10,83,87,1,87,6,91,2,9,91,95,1,95,5,99,1,5,99,103,1,103,10,107,1,9,107,111,1,6,111,115,1,115,5,119,1,10,119,123,2,6,123,127,2,127,6,131,1,131,2,135,1,10,135,0,99,2,0,14,0])
    run_program([1,98,20,3,1,1,2,3,1,3,4,3,1,5,0,3,2,10,1,19,1,6,19,23,1,23,13,27,2,6,27,31,1,5,31,35,2,10,35,39,1,6,39,43,1,13,43,47,2,47,6,51,1,51,5,55,1,55,6,59,2,59,10,63,1,63,6,67,2,67,10,71,1,71,9,75,2,75,10,79,1,79,5,83,2,10,83,87,1,87,6,91,2,9,91,95,1,95,5,99,1,5,99,103,1,103,10,107,1,9,107,111,1,6,111,115,1,115,5,119,1,10,119,123,2,6,123,127,2,127,6,131,1,131,2,135,1,10,135,0,99,2,0,14,0])


if __name__ == "__main__":
    main()
