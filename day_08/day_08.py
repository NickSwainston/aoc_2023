
import numpy as np
from itertools import count
from math import lcm

if __name__ == "__main__":
    # with open('example_1.txt', 'r') as file:
    # with open('example_2.txt', 'r') as file:
    # with open('example_3.txt', 'r') as file:
    with open('input.txt', 'r') as file:
        # Read the lines
        lines = file.readlines()
        lines = [line.strip() for line in lines]

    steps = [char for char in lines[0]]
    network = {}
    for line in lines[2:]:
        start = line.split(" = ")[0]
        left, right = line.split(" = ")[1][1:-1].split(", ")
        network[start] = [left, right]

    # current = "AAA"
    # step_count = 0
    # while current != "ZZZ":
    #     for step in steps:
    #         step_count += 1
    #         # print(f"Step {step_count}")
    #         # print(f"Current: {current}")
    #         if step == "L":
    #             current = network[current][0]
    #         elif step == "R":
    #             current = network[current][1]
    #         if current == "ZZZ":
    #             break
    # print(f"Current: {current}")

    # print(f"Part 1: {step_count}")

    start_points = []
    for key in network.keys():
        if key.endswith("A"):
            start_points.append(key)
    all_nodes = np.array(start_points)

    def move_node_left(x):
        return network[x][0]
    vectorized_move_node_left = np.vectorize(move_node_left)
    def move_node_right(x):
        return network[x][1]
    vectorized_move_node_right = np.vectorize(move_node_right)

    first_two = np.zeros((len(start_points), 2))
    step_count = 0
    all_end_with_z = np.char.endswith(all_nodes, 'Z')
    all_second_found = np.all(first_two[:, 1] != 0)
    while not all_second_found:
        for step in steps:
            step_count += 1
            # print(f"Step {step_count}")
            # print(f"Current: {current}")
            if step == "L":
                all_nodes = vectorized_move_node_left(all_nodes)
            elif step == "R":
                all_nodes = vectorized_move_node_right(all_nodes)
            # print(all_nodes)
            all_end_with_z = np.char.endswith(all_nodes, 'Z')
            for i, node_bool in enumerate(all_end_with_z):
                if node_bool:
                    if first_two[i, 0] == 0:
                        first_two[i, 0] = step_count
                    elif first_two[i, 1] == 0:
                        first_two[i, 1] = step_count
            all_second_found = np.all(first_two[:, 1] != 0)
    print(first_two)
    offsets = []
    loops = []
    for pair in first_two:
        offsets.append(int(pair[0]))
        loops.append(int(pair[1] - pair[0]))
    lcm_loops = lcm(*loops)
    print(f"LCM of loops: {lcm_loops}")
    offsets.append(lcm_loops)
    lcm_offsets = lcm(*offsets)
    print(f"LCM of offsets: {lcm_offsets}")
    print(f"Part 2: {lcm_offsets}")

    print(f"Part 2: {step}")



