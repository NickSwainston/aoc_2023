# with open('example.txt', 'r') as file:
with open('input.txt', 'r') as file:
    # Read the lines
    lines = file.readlines()
    lines = [line.strip() for line in lines]

chunks = []
current_chunk = []
for line in lines:
    if line.strip():  # If the line is not blank
        current_chunk.append(line)
    else:
        if current_chunk:
            chunks.append(current_chunk)
            current_chunk = []
if current_chunk:
    chunks.append(current_chunk)


seeds = [int(seed) for seed in chunks[0][0].split()[1:]]
print(seeds)

all_maps = []
for chunk in chunks[1:]:
    print(f"Chunk: {chunk}")
    current_map = []
    for line in chunk[1:]:
        dest_start, source_start, length = [int(value) for value in line.split()]
        current_map.append((source_start, source_start + length, dest_start - source_start))
    all_maps.append(current_map)

locations = []
for seed in seeds:
    print(f"\nSeed: {seed}")
    current_value = seed
    for current_map in all_maps:
        for start, end, change in current_map:
            if start <= current_value <= end:
                current_value += change
                break
        print(current_value)
    locations.append(current_value)

print(f"Part 1 {min(locations)}")


inverse_maps = []
for chunk in reversed(chunks[1:]):
    print(f"Chunk: {chunk}")
    current_map = []
    for line in chunk[1:]:
        dest_start, source_start, length = [int(value) for value in line.split()]
        current_map.append((dest_start, dest_start + length, source_start- dest_start))
    inverse_maps.append(current_map)
print(all_maps)
print(inverse_maps)


possible_location = 0
found_seed = False
while not found_seed:
    possible_location += 1
    print(f"\nPossible location: {possible_location}")
    current_value = possible_location
    for inverse_map in inverse_maps:
        for start, end, change in inverse_map:
            if start <= current_value <= end:
                current_value += change
                break
    # print(f"Seed value: {current_value}")
    is_a_seed = False
    for i in range(len(seeds)//2):
        left_range, right_range = (seeds[2*i], seeds[2*i] + seeds[2*i+1] - 1)
        # print(f"Left range: {left_range}, right range: {right_range}")
        if left_range <= current_value <= right_range:
            # print(f"Found seed: {seeds[i]}")
            is_a_seed = True
            break
    if is_a_seed:
        found_seed = True

print(f"Part 2 {possible_location}")