# with open('example.txt', 'r') as file:
with open('input.txt', 'r') as file:
    # Read the lines
    lines = file.readlines()
    lines = [line.strip() for line in lines]

game_sum = 0
smallest_colours_sum = 0
for line in lines:
    game_id, subsets = line.split(':')
    game_id = int(game_id.split()[1])
    subsets = subsets.split(';')
    possible = True
    smallest_red = 0
    smallest_green = 0
    smallest_blue = 0
    for subset in subsets:
        colours = subset.split(",")
        for colour in colours:
            if "red" in colour:
                red_value = int(colour.split()[0].strip())
                if red_value > 12:
                    possible = False
                if red_value > smallest_red:
                    smallest_red = red_value
            elif "green" in colour:
                green_value = int(colour.split()[0].strip())
                if green_value > 13:
                    possible = False
                if green_value > smallest_green:
                    smallest_green = green_value
            elif "blue" in colour:
                blue_value = int(colour.split()[0].strip())
                if blue_value > 14:
                    possible = False
                if blue_value > smallest_blue:
                    smallest_blue = blue_value
    if possible:
        game_sum += game_id
    print(game_id, smallest_red, smallest_green, smallest_blue)
    smallest_colours_sum += smallest_red * smallest_green * smallest_blue

print(f"Part 1: {game_sum}")
print(f"Part 2: {smallest_colours_sum}")


