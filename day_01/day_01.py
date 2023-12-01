# with open('example2.txt', 'r') as file:
with open('input.txt', 'r') as file:
    # Read the lines
    lines = file.readlines()
    lines = [line.strip() for line in lines]

sum1 = 0
for line in lines:
    for char in line:
        if char.isdigit():
            first_digit = char
            break
    for char in reversed(line):
        if char.isdigit():
            last_digit = char
            break
    sum1 += int(f"{first_digit}{last_digit}")

print(f"Part 1: {sum1}")

numbers = {
    "one": 1,
    "two": 2,
    'three': 3,
    "four": 4,
    "five": 5,
    "six": 6,
    "seven": 7,
    "eight": 8,
    "nine": 9,
}

sum2 = 0
for line in lines:
    line_numbers = []
    for i in range(len(line)):
        subline = line[i:]
        if line[i].isdigit():
            line_numbers.append(int(line[i]))
        for number in numbers.keys():
            if subline.startswith(number):
                line_numbers.append(numbers[number])
    sum2 += int(f"{line_numbers[0]}{line_numbers[-1]}")

print(f"Part 2: {sum2}")