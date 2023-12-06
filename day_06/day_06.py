# with open('example.txt', 'r') as file:
with open('input.txt', 'r') as file:
    # Read the lines
    lines = file.readlines()
    lines = [line.strip() for line in lines]

times = [int(i) for i in lines[0].split()[1:]]
distances = [int(i) for i in lines[1].split()[1:]]

options_sum = 1
for time, distance in zip(times, distances):
    options = 0
    for time_hold in range(1, time):
        time_left = time - time_hold
        speed = time_hold
        time_to_finish = distance / speed
        if time_to_finish < time_left:
            # print(f"Time hold: {time_hold}, speed: {speed}, time to finish: {time_to_finish}")
            options += 1
    options_sum *= options

    print(f"Time: {time}, distance: {distance}, options: {options}")
print(f"Part 1: {options_sum}")


time = int("".join(lines[0].split()[1:]))
distance = int("".join(lines[1].split()[1:]))

options = 0
for time_hold in range(1, time):
    time_left = time - time_hold
    speed = time_hold
    time_to_finish = distance / speed
    if time_to_finish < time_left:
        # print(f"Time hold: {time_hold}, speed: {speed}, time to finish: {time_to_finish}")
        options += 1

    # print(f"Time: {time}, distance: {distance}, options: {options}")
print(f"Part 2: {options}")