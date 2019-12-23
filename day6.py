"""
Advent of Code 2019
Day 6
"""

from anytree import Node, RenderTree, PreOrderIter, Walker


def read_star_map(path):
    with open(path, "r") as input_file:
        raw_map = [line.strip("\n") for line in input_file]
        unique_stars = list(set([line.split(sep=")")[0] for line in raw_map] + [line.split(sep=")")[1] for line in raw_map]))

    return raw_map, unique_stars


def main():
    raw_map, unique_stars = read_star_map("day6test.txt")

    # Star map contains tree nodes, children contains the children names of each star, parents contains parent names
    # for each star. The key for these values is the star's name.
    star_map = {star: Node(name=star) for star in unique_stars}
    children = {star: list() for star in unique_stars}
    parents = {star: None for star in unique_stars}

    # Iterate through the raw map and assess the parent/children of each star.
    for line in raw_map:
        # Split the line into parent)child
        parent = line.split(sep=")")[0]
        child = line.split(sep=")")[1]

        # Append the parent and child names for each star on the line to the relevant dictionaries.
        children[parent].append(child)
        parents[child] = parent

    # Create tree nodes.
    for star in unique_stars:
        star_node = star_map[star]

        if star != "COM":
            parent_node = star_map[parents[star]]
            star_node.parent = parent_node

        child_nodes = [star_map[child] for child in children[star]]
        star_node.children = child_nodes

    # Print the tree
    # for pre, fill, node in RenderTree(star_map["COM"]):
    #     print("%s%s" % (pre, node.name))

    # Count the number of orbits by walking the tree.
    count = 0
    stars = [star.name for star in PreOrderIter(star_map["COM"])]
    for star in stars:
        for step in PreOrderIter(star_map[star]):
            count += 1

    count -= len(stars)
    print(count)

    # Walk from YOU to SAN
    w = Walker()
    upwards, _, downwards = w.walk(star_map["YOU"], star_map["SAN"])
    journey = list(upwards + downwards)
    print(len(journey) - 2)


if __name__ == "__main__":
    main()
