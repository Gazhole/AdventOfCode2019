"""
Advent of Code 2019
Day 1
"""


def load(path):
    with open(path, "r") as inputfile:
        return [int(module.strip("\n")) for module in inputfile]


def calculate_fuel(module):
    return int(module / 3) - 2


def main():
    modules = load("input_day1.txt")
    total_fuel = sum([calculate_fuel(module) for module in modules])
    print(total_fuel)


if __name__ == "__main__":
    main()
