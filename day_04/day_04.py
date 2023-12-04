# with open('example.txt', 'r') as file:
with open('input.txt', 'r') as file:
    # Read the lines
    lines = file.readlines()
    lines = [line.strip() for line in lines]

win_sum = 0
for line in lines:
    card_number = line.split(":")[0]
    card_number = int(card_number.split()[1])
    winning_numbers = line.split(":")[1].split("|")[0].strip()
    winning_numbers = [int(num) for num in winning_numbers.split()]
    our_numbers = line.split(":")[1].split("|")[1].strip()
    our_numbers = [int(num) for num in our_numbers.split()]
    wins = 0
    for num in our_numbers:
        if num in winning_numbers:
            wins += 1
    if wins > 0:
        win_sum += 2**(wins-1)

print(f"Part 1: {win_sum}")

card_copies = {}
for i in range(1, len(lines)+1):
    card_copies[i] = 1
for card_number in card_copies.keys():

    winning_numbers = lines[card_number-1].split(":")[1].split("|")[0].strip()
    winning_numbers = [int(num) for num in winning_numbers.split()]
    our_numbers = lines[card_number-1].split(":")[1].split("|")[1].strip()
    our_numbers = [int(num) for num in our_numbers.split()]
    wins = 0
    for num in our_numbers:
        if num in winning_numbers:
            wins += 1
    for i in range(card_number + 1, card_number + 1 + wins):
        print(i)
        card_copies[i] += card_copies[card_number]

total_sum = 0
for card_number in card_copies.keys():
    print(card_number, card_copies[card_number])
    total_sum += card_copies[card_number]

print(f"Part 2: {total_sum}")