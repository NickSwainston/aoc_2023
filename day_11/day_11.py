import numpy as np

def get_path_between(coord_1, coord_2):
    x = abs(coord_1[0] - coord_2[0])
    y = abs(coord_1[1] - coord_2[1])
    return x + y


def part_1(lines):

    galaxies = []
    for line in lines:
        gal_line = [char for char in line]
        galaxies.append(gal_line)
        if all(element == '.' for element in gal_line):
            # Add extra space rows
            galaxies.append(gal_line)
    galaxies = np.array(galaxies)

    # Add extra space columns
    space_columns = []
    for coli in range(galaxies.shape[1]):
        if np.all(galaxies[:, coli] == '.'):
            space_columns.append(coli)
    for i, coli in enumerate(space_columns):
        galaxies = np.insert(galaxies, coli+i, '.', axis=1)

    galaxy_locs = []
    for y in range(galaxies.shape[0]):
        for x in range(galaxies.shape[1]):
            if galaxies[y, x] == '#':
                galaxy_locs.append((x, y))

    for i, loc in enumerate(galaxy_locs):
        galaxies[loc[1], loc[0]] = i + 1
        print(f"Galaxy {i+1} at {loc}")

    print(galaxies)

    path_sum = 0
    for i in range(len(galaxy_locs)):
        for j in range(i+1, len(galaxy_locs)):
            path_sum += get_path_between(galaxy_locs[i], galaxy_locs[j])
    return path_sum


def part_2(lines):

    galaxies = []
    for line in lines:
        gal_line = [char for char in line]
        galaxies.append(gal_line)
    galaxies = np.array(galaxies)

    galaxy_locs = []
    for y in range(galaxies.shape[0]):
        for x in range(galaxies.shape[1]):
            if galaxies[y, x] == '#':
                galaxy_locs.append((x, y))
    print(galaxies)

    space_columns = []
    for coli in range(galaxies.shape[1]):
        if np.all(galaxies[:, coli] == '.'):
            space_columns.append(coli)
    space_rows = []
    for rowi in range(galaxies.shape[0]):
        if np.all(galaxies[rowi, :] == '.'):
            space_rows.append(rowi)
    print(space_rows, space_columns)

    spaced_galaxy_locs = []
    space_size = 1000000 - 1
    for gal_x, gal_y in galaxy_locs:
        new_gal_x = gal_x
        new_gal_y = gal_y
        for space_row in space_rows:
            if space_row < gal_y:
                new_gal_y += space_size
        for space_col in space_columns:
            if space_col < gal_x:
                new_gal_x += space_size
        spaced_galaxy_locs.append((new_gal_x, new_gal_y))
    print(galaxy_locs)
    print(spaced_galaxy_locs)

    path_sum = 0
    for i in range(len(spaced_galaxy_locs)):
        for j in range(i+1, len(spaced_galaxy_locs)):
            path_sum += get_path_between(spaced_galaxy_locs[i], spaced_galaxy_locs[j])
    return path_sum


if __name__ == "__main__":
    # with open('example.txt', 'r') as file:
    with open('input.txt', 'r') as file:
        # Read the lines
        lines = file.readlines()
        lines = [line.strip() for line in lines]

    assert get_path_between((1, 6), (5, 11)) == 9
    assert get_path_between((4, 0), (9, 10)) == 15
    assert get_path_between((0, 2), (12, 7)) == 17
    assert get_path_between((0, 11), (5, 11)) == 5

    path_sum = part_1(lines)

    print(f"Part 1: {path_sum}")
    path_sum = part_2(lines)

    print(f"Part 2: {path_sum}")

