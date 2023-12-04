import numpy as np

# with open('example.txt', 'r') as file:
with open('input.txt', 'r') as file:
    # Read the lines
    lines = file.readlines()
    lines = [line.strip() for line in lines]

serial_numbers = {}
symbol_locations = []
gears = []
for yi, line in enumerate(lines):
    temp_num = ""
    temp_coords = []
    for xi, char in enumerate(line):
        if char.isdigit():
            temp_num += char
            temp_coords.append((xi, yi))
        else:
            if temp_num != "" and not char.isdigit():
                serial_numbers[f"{temp_num}_{temp_coords[0][0]}_{temp_coords[0][1]}"] = temp_coords
                temp_num = ""
                temp_coords = []
        if not char.isdigit() and char != ".":
            symbol_locations.append((xi, yi))
        if char == "*":
            gears.append((xi, yi))
    if temp_num != "":
        serial_numbers[f"{temp_num}_{temp_coords[0][0]}_{temp_coords[0][1]}"] = temp_coords

# print(serial_numbers)
# print(symbol_locations)

serial_sum = 0
for serial_num in serial_numbers.keys():
    real = False
    serial_locations = serial_numbers[serial_num]
    for ser_x, ser_y in serial_locations:
        for sym_x, sym_y in symbol_locations:
            distance = np.sqrt(abs(ser_x - sym_x)**2 + abs(ser_y - sym_y)**2)
            if distance < 1.5:
                real = True
    if real:
        serial_sum += int(serial_num.split("_")[0])

print(f"Part 1: {serial_sum}")

gear_sum = 0
for gear_x, gear_y in gears:
    nearby_serials = []
    for serial_num in serial_numbers.keys():
        serial_locations = serial_numbers[serial_num]
        for ser_x, ser_y in serial_locations:
            distance = np.sqrt(abs(ser_x - gear_x)**2 + abs(ser_y - gear_y)**2)
            this_serial = int(serial_num.split("_")[0])
            if distance < 1.5 and this_serial not in nearby_serials:
                nearby_serials.append(this_serial)
    if len(nearby_serials) == 2:
        gear_sum += nearby_serials[0] * nearby_serials[1]

print(f"Part 2: {gear_sum}")