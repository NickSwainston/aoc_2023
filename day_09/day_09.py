import numpy as np


if __name__ == "__main__":
    # with open('example.txt', 'r') as file:
    with open('input.txt', 'r') as file:
        # Read the lines
        lines = file.readlines()
        patterns = [line.strip() for line in lines]

    total_end = 0
    total_start = 0
    for pattern in patterns:
        pattern = [int(char) for char in pattern.split()]
        pattern_tree = [pattern]
        current_pattern = np.array(pattern)
        while not np.all(current_pattern == 0):
            print(current_pattern)
            new_pattern = []
            for i in range(len(current_pattern) - 1):
                new_pattern.append(current_pattern[i+1] - current_pattern[i])
            pattern_tree.append(new_pattern)
            current_pattern = np.array(new_pattern)

        current_value = 0
        for i, pattern in enumerate(reversed(pattern_tree)):
            current_value = pattern[-1] + current_value
            # print(i, current_value)
        total_end += current_value

        current_value = 0
        for i, pattern in enumerate(reversed(pattern_tree)):
            current_value = pattern[0] - current_value
            print(i, current_value)
        total_start += current_value
    print("Part 1:", total_end)
    print("Part 2:", total_start)