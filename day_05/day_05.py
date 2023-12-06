with open('example.txt', 'r') as file:
# with open('input.txt', 'r') as file:
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

locations = []
for i in range(len(seeds)//2):
    edges = [(seeds[i], seeds[i] + seeds[i+1] - 1)]
    print(f"Seed range: {edges}")
    for current_map in all_maps:
        this_maps_edges = []
        for input_start, input_end in edges:
            print(f"    Input range: {input_start} - {input_end}")
            if (input_start, input_end) not in this_maps_edges:
                this_maps_edges.append((input_start, input_end))
            for start, end, change in current_map:
                print(f"        Map range: {start} - {end}")
                if start < input_start and input_end < end:
                    print("        Inside")
                    pass
                elif input_start < start and end < input_end:
                    print("        Outside")
                    try:
                        this_maps_edges.remove((input_start, input_end))
                    except ValueError:
                        pass
                    this_maps_edges.append((input_start, start -1))
                    this_maps_edges.append((start, end -1))
                    this_maps_edges.append((end, input_end -1))

                elif input_start < start < input_end:
                    print("        Start inside")
                    try:
                        this_maps_edges.remove((input_start, input_end))
                    except ValueError:
                        pass
                    this_maps_edges.append((input_start, start -1))
                    this_maps_edges.append((start, input_end))
                elif input_start < end < input_end:
                    print("        End inside")
                    try:
                        this_maps_edges.remove((input_start, input_end))
                    except ValueError:
                        pass
                    this_maps_edges.append((input_start, end -1))
                    this_maps_edges.append((end, input_end))
                else:
                    print("        No overlap")
                    pass
                print(f"        this_maps_edges: {this_maps_edges}")

        new_edge_values = []
        for edge_start, edge_stop in this_maps_edges:
            for start, end, change in current_map:
                if start <= edge_start <= end:
                    edge_start += change
                    break
            for start, end, change in current_map:
                if start <= edge_stop <= end:
                    edge_stop += change
                    break
            new_edge_values.append((edge_start, edge_stop))
        edges = new_edge_values
        print(f"New edges: {edges}")
    print(f"Final edges: {edges}")
    for start, end in edges:
        locations.append(start)
        locations.append(end)

print(f"Part 2 {min(locations)}")