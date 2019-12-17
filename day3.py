"""
Advent of Code 2019
Day 3
"""


class PathTracer:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.coords = list()

    def move(self, direction, distance):
        new_coords = list()
        if direction == "U":
            new_x = self.x
            new_y = self.y + distance
            key = 1
            reverse = False
        elif direction == "D":
            new_x = self.x
            new_y = self.y - distance
            key = 1
            reverse = True
        elif direction == "L":
            new_y = self.y
            new_x = self.x - distance
            key = 0
            reverse = True
        elif direction == "R":
            new_y = self.y
            new_x = self.x + distance
            key = 0
            reverse = False

        for x in range(min(self.x, new_x), max(self.x, new_x) + 1):
            for y in range(min(self.y, new_y), max(self.y, new_y) + 1):
                new_coords.append((x, y))

        new_coords = sorted(new_coords, key=lambda tup: tup[key], reverse=reverse)
        new_coords.pop()
        self.coords.extend(new_coords)
        self.x = new_x
        self.y = new_y


def load_wires(file_path):
    wires = dict()
    with open(file_path, "r") as input_file:
        for idx, line in enumerate(input_file):
            wires[idx] = tuple(line.split(","))
    return wires


def trace_paths(wires):
    results = dict()
    for wire_number in sorted(wires.keys()):
        this_wire = wires[wire_number]
        tracer = PathTracer()

        for instruction in this_wire:
            direction = instruction[0]
            distance = int(instruction[1::])
            tracer.move(direction, distance)

        results[wire_number] = tracer
    return results


def find_intersections(paths):
    wire_0 = set(paths[0].coords)
    wire_1 = set(paths[1].coords)
    intersections = wire_0.intersection(wire_1)
    return list(intersections)


def calculate_steps(paths, intersections):
    wire_0 = paths[0].coords
    wire_1 = paths[1].coords

    wire_0_results = dict()
    wire_1_results = dict()
    for intersection in intersections:
        wire_0_count = 0
        wire_1_count = 0

        for step in wire_0:
            if step == intersection:
                wire_0_results[intersection] = wire_0_count
            else:
                wire_0_count += 1

        for step in wire_1:
            if step == intersection:
                wire_1_results[intersection] = wire_1_count
            else:
                wire_1_count += 1

    return wire_0_results, wire_1_results


def find_quickest_path(wire_0_steps, wire_1_steps, intersections):
    x = {i: wire_0_steps[i] + wire_1_steps[i] for i in intersections if wire_0_steps[i] + wire_0_steps[i] > 0}
    return min(x.values())


def calculate_closest_intersection(intersections):
    distances = list()
    for coord in intersections:
        x = coord[0]
        y = coord[1]

        if x < 0:
            x = x * -1

        if y < 0:
            y = y * -1

        distances.append((x, y))

    return min([sum(list(coord)) for coord in distances if sum(list(coord)) > 0])


def main():
    wires = load_wires("input day 3")
    paths = trace_paths(wires)
    intersections = find_intersections(paths)
    answer1 = calculate_closest_intersection(intersections)
    print(answer1)
    wire_0_steps, wire_1_steps = calculate_steps(paths, intersections)
    answer2 = find_quickest_path(wire_0_steps, wire_1_steps, intersections)
    print(answer2)


if __name__ == "__main__":
    main()
