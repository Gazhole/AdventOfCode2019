"""
Advent of Code 2019
Day 1
"""


def load(path):
    with open(path, "r") as inputfile:
        return [int(module.strip("\n")) for module in inputfile]


def calculate_fuel(module):
    total_fuel = 0
    fuel = int(module / 3) - 2
    while fuel > 0:
        total_fuel += fuel
        fuel = int(fuel / 3) - 2
    return total_fuel


def main():
    modules = load("input_day1.txt")
    total_fuel = sum([calculate_fuel(module) for module in modules])
    print(total_fuel)


if __name__ == "__main__":
    main()
