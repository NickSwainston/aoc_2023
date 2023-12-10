
import numpy as np

def read_in_start_points(input_file):
    with open(input_file, 'r') as file:
        lines = file.readlines()
        lines = [line.strip() for line in lines]

    pipes =[]
    for line in lines:
        pipe = [char.replace("L", "┖").replace("J", "┙").replace("7", "┑").replace("F", "┍") for char in line]
        print("".join(pipe))
        pipes.append(pipe)

    pipes = np.array(pipes)
    start_point = np.where(pipes == "S")
    start_point_x = start_point[1][0]
    start_point_y = start_point[0][0]
    print(pipes[start_point_y][start_point_x])
    assert "S" == pipes[start_point_y][start_point_x]
    print(start_point)

    start_points = []
    for x in range(pipes.shape[1]):
        for y in range(pipes.shape[0]):
            pipe = pipes[y][x]
            distance = np.sqrt(abs(start_point_x - x)**2 + abs(start_point_y - y)**2)
            if distance == 1.:
                # Neabry so check if connected
                if start_point_x - x == 1 and start_point_y - y == 0:
                    #Left up
                    print(f"Left pipe: {pipe}")
                    if pipe == "┖" or pipe == "┍" or pipe == "-":
                        start_points.append((x,y))
                if start_point_x - x == -1 and start_point_y - y == 0:
                    # Right
                    print(f"Right pipe: {pipe}")
                    if pipe == "┙" or pipe == "┑" or pipe == "-":
                        start_points.append((x,y))
                if start_point_x - x == 0 and start_point_y - y == 1:
                    # Up
                    print(f"Up pipe: {pipe}")
                    if pipe == "┑" or pipe == "┍" or pipe == "|":
                        start_points.append((x,y))
                if start_point_x - x == 0 and start_point_y - y == -1:
                    # Down
                    print(f"Down pipe: {pipe}")
                    if pipe == "┖" or pipe == "┙" or pipe == "|":
                        start_points.append((x,y))
    print(start_points)
    return pipes, start_points, start_point_x, start_point_y

def find_max_distance(input_file):
    pipes, start_points, start_point_x, start_point_y = read_in_start_points(input_file)
    distances = np.zeros_like(pipes, dtype=int)
    for this_start_point_x, this_start_point_y in start_points:
        end = False
        distance = 0
        prev_x = start_point_x
        prev_y = start_point_y
        curr_x = this_start_point_x
        curr_y = this_start_point_y
        while not end:
            distance += 1
            # print(distance)
            pipe = pipes[curr_y][curr_x]
            # print(pipe, curr_x, curr_y)
            # Check for edges
            if pipe == "S":
                print("Returned to start at point ", pipe, curr_x, curr_y)
                end = True
                break
            elif curr_x < 0 or curr_x == pipes.shape[0]:
                print("Hit x edge at point ", pipe, curr_x, curr_y)
                end = True
                break
            elif curr_y < 0 or curr_y == pipes.shape[1]:
                print("hit y edge at point ", pipe, curr_x, curr_y)
                end = True
                break
            # update curr pipe distance
            # if distances[curr_y][curr_x] == "":
            #     distances[curr_y][curr_x] = distance
            if distances[curr_y][curr_x] > int(distance) or distances[curr_y][curr_x] == 0:
                distances[curr_y][curr_x] = distance
            # print(distances)
            # Work out where next pipe goes
            if pipe == "|":
                if prev_y - curr_y == 1:
                    # Going up
                    prev_y = curr_y
                    curr_y += -1
                else:
                    # Going down
                    prev_y = curr_y
                    curr_y += 1
            elif pipe == "-":
                if prev_x - curr_x == 1:
                    # Going left
                    prev_x = curr_x
                    curr_x += -1
                else:
                    # Going right
                    prev_x = curr_x
                    curr_x += 1
            elif pipe == "┖":
                if prev_y - curr_y == -1:
                    # Going down
                    prev_x = curr_x
                    prev_y = curr_y
                    curr_x += 1
                else:
                    # Going left
                    prev_x = curr_x
                    prev_y = curr_y
                    curr_y += -1
            elif pipe == "┙":
                if prev_y - curr_y == -1:
                    # Going down
                    prev_x = curr_x
                    prev_y = curr_y
                    curr_x += -1
                else:
                    # Going right
                    prev_x = curr_x
                    prev_y = curr_y
                    curr_y += -1
            elif pipe == "┑":
                if prev_y - curr_y == 1:
                    # Going up
                    prev_y = curr_y
                    prev_x = curr_x
                    curr_x += -1
                else:
                    # Going right
                    prev_x = curr_x
                    prev_y = curr_y
                    curr_y += 1
            elif pipe == "┍":
                if prev_y - curr_y == 1:
                    # Going up
                    prev_y = curr_y
                    prev_x = curr_x
                    curr_x += 1
                else:
                    # Going left
                    prev_x = curr_x
                    prev_y = curr_y
                    curr_y += 1
    np.set_printoptions(threshold=np.inf)
    # print(distances)
    return distances.max()

def find_inside_points(input_file):
    pipes, start_points, start_point_x, start_point_y = read_in_start_points(input_file)


    # Remove all unused pipe
    used_pipes = np.full_like(pipes, fill_value=".")
    for this_start_point_x, this_start_point_y in start_points:
        end = False
        distance = 0
        prev_x = start_point_x
        prev_y = start_point_y
        curr_x = this_start_point_x
        curr_y = this_start_point_y
        while not end:
            # print(distance)
            pipe = pipes[curr_y][curr_x]
            # print(pipe, curr_x, curr_y)
            # Check for edges
            if pipe == "S":
                print("Returned to start at point ", pipe, curr_x, curr_y)
                end = True
                break
            elif curr_x < 0 or curr_x == pipes.shape[1]:
                print("Hit x edge at point ", pipe, curr_x, curr_y)
                end = True
                break
            elif curr_y < 0 or curr_y == pipes.shape[0]:
                print("hit y edge at point ", pipe, curr_x, curr_y)
                end = True
                break
            # update curr pipe distance
            # if distances[curr_y][curr_x] == "":
            #     distances[curr_y][curr_x] = distance
            used_pipes[curr_y][curr_x] = pipe
            # print(distances)
            # Work out where next pipe goes
            if pipe == "|":
                if prev_y - curr_y == 1:
                    # Going up
                    prev_y = curr_y
                    curr_y += -1
                else:
                    # Going down
                    prev_y = curr_y
                    curr_y += 1
            elif pipe == "-":
                if prev_x - curr_x == 1:
                    # Going left
                    prev_x = curr_x
                    curr_x += -1
                else:
                    # Going right
                    prev_x = curr_x
                    curr_x += 1
            elif pipe == "┖":
                if prev_y - curr_y == -1:
                    # Going down
                    prev_x = curr_x
                    prev_y = curr_y
                    curr_x += 1
                else:
                    # Going left
                    prev_x = curr_x
                    prev_y = curr_y
                    curr_y += -1
            elif pipe == "┙":
                if prev_y - curr_y == -1:
                    # Going down
                    prev_x = curr_x
                    prev_y = curr_y
                    curr_x += -1
                else:
                    # Going right
                    prev_x = curr_x
                    prev_y = curr_y
                    curr_y += -1
            elif pipe == "┑":
                if prev_y - curr_y == 1:
                    # Going up
                    prev_y = curr_y
                    prev_x = curr_x
                    curr_x += -1
                else:
                    # Going right
                    prev_x = curr_x
                    prev_y = curr_y
                    curr_y += 1
            elif pipe == "┍":
                if prev_y - curr_y == 1:
                    # Going up
                    prev_y = curr_y
                    prev_x = curr_x
                    curr_x += 1
                else:
                    # Going left
                    prev_x = curr_x
                    prev_y = curr_y
                    curr_y += 1
    pipes = used_pipes


    # Replace the S with a pipe
    start_point_directions = []
    for this_start_point_x, this_start_point_y in start_points:
        if this_start_point_x - start_point_x == 1:
            start_point_directions.append("right")
        if this_start_point_x - start_point_x == -1:
            start_point_directions.append("left")
        if this_start_point_y - start_point_y == -1:
            start_point_directions.append("up")
        if this_start_point_y - start_point_y == 1:
            start_point_directions.append("down")
    if "left" in start_point_directions and "right" in start_point_directions:
        pipes[start_point_y][start_point_x] = "-"
    elif "up" in start_point_directions and "down" in start_point_directions:
        pipes[start_point_y][start_point_x] = "|"
    elif "right" in start_point_directions and "down" in start_point_directions:
        pipes[start_point_y][start_point_x] = "┍"
    elif "left" in start_point_directions and "down" in start_point_directions:
        pipes[start_point_y][start_point_x] = "┑"
    elif "right" in start_point_directions and "up" in start_point_directions:
        pipes[start_point_y][start_point_x] = "┖"
    elif "left" in start_point_directions and "up" in start_point_directions:
        pipes[start_point_y][start_point_x] = "┙"
    print(pipes)



    y_in = np.zeros_like(pipes, dtype=int)
    x_in = np.zeros_like(pipes, dtype=int)
    start_edge= False
    end_edge = False
    for x in range(pipes.shape[1]):
        in_y = False
        for y in range(pipes.shape[0]):
            pipe = pipes[y][x]
            if pipe in ["┑", "┍", "S"]:
                start_edge= True
            if pipe in ["┖", "┙", "S"]:
                end_edge= True
            else:
                end_edge = False
            if start_edge and not end_edge:
                # Do nothing until found edge
                continue
            elif start_edge and end_edge:
                # found edge so reset
                start_edge = False
                continue
            elif pipe == "-":
                # Switch in out bool
                in_y = not in_y
            elif not start_edge and not end_edge:
                if in_y:
                    # mark as in
                    y_in[y][x] = 1
    start_edge= False
    end_edge = False
    for y in range(pipes.shape[0]):
        in_x = False
        for x in range(pipes.shape[1]):
            pipe = pipes[y][x]
            if pipe in ["┖", "┍"]:
                start_edge= True
                start_pipe = pipe
            if pipe in ["┙", "┑"]:
                end_edge= True
            else:
                end_edge = False
            if start_edge and not end_edge:
                # Do nothing until found edge
                continue
            elif start_edge and end_edge:
                # found edge so reset
                start_edge = False
                if pipe == "┙" and start_pipe == "┍" or \
                   pipe == "┑" and start_pipe == "┖":
                    # s shape so switch
                    in_x = not in_x
            elif pipe == "|":
                # Switch in out bool
                in_x = not in_x
            elif not start_edge and not end_edge:
                if in_x:
                    # mark as in
                    x_in[y][x] = 1

    print("x_in")
    print(x_in)
    # print("y_in")
    # print(y_in)
    # indices_boolean = np.where((x_in == 1) & (y_in == 1))
    # print(indices_boolean)
    # # Using numpy.where
    # indices_where = np.where(np.logical_and(x_in == 1, y_in == 1))
    # print(indices_where)
    return np.sum(x_in)



if __name__ == "__main__":
    assert find_max_distance("example_1.txt") == 4
    assert find_max_distance("example_2.txt") == 8
    max_distance = find_max_distance("input.txt")
    print(f"Part 1: {max_distance}")
    assert find_inside_points("example_3.txt") == 4
    assert find_inside_points("example_4.txt") == 8
    assert find_inside_points("example_5.txt") == 10
    inside_points = find_inside_points("input.txt")
    print(f"Part 2: {inside_points}")

