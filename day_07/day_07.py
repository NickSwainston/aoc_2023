import numpy as np


def calc_winings(hand_bids, cards):
    print(cards)
    rank = 1
    winnings = 0
    hand_type_order = [
        "five of a kind",
        "four of a kind",
        "full house",
        "three of a kind",
        "two pairs",
        "one pair",
        "nothing"
    ]
    for rank_hand_tpye in reversed(hand_type_order):
        this_rank = []
        for hand, bid, hand_type in hand_bids:
            if hand_type == rank_hand_tpye:
                this_rank.append((hand, bid, hand_type))
        if len(this_rank) == 1:
            winnings += this_rank[0][1] * rank
            print("Only one best")
            print(f"    Won: {this_rank[0][1]} * {rank} = {this_rank[0][1] * rank}")
            rank += 1
        elif len(this_rank) > 1:
            print("Finding best of multiple")
            hand_values = np.empty((len(this_rank), 6))
            for hand_i, this_hand in enumerate(this_rank):
                for card_i, this_card in enumerate(this_hand[0]):
                    for card_value, card in enumerate(cards):
                        if this_card == card:
                            hand_values[hand_i, card_i] = int(card_value)

                hand_values[hand_i, 5] = int(this_hand[1]) # add the actual bid of the hand
            bid_value_pairs = []
            for this_hand in hand_values:
                card_value = int(f"{int(this_hand[0]):02d}{int(this_hand[1]):02d}{int(this_hand[2]):02d}{int(this_hand[3]):02d}{int(this_hand[4]):02d}")
                bid_value_pairs.append([this_hand[5], card_value])
            sorted_list = sorted(bid_value_pairs, key=lambda x: x[1])
            for this_hand in sorted_list:
                # print(f"    {this_hand}")
                # print(f"    Won: {this_hand[0]} * {rank} = {this_hand[0] * rank}")
                winnings += int(this_hand[0]) * rank
                rank += 1
    return winnings

def hand_type_2(hand):
    possibilities = {
        "A": 0,
        "K": 0,
        "Q": 0,
        "J": 0,
        "T": 0,
        "9": 0,
        "8": 0,
        "7": 0,
        "6": 0,
        "5": 0,
        "4": 0,
        "3": 0,
        "2": 0,
    }
    for card in hand:
        possibilities[card[0]] += 1

    pos_no_j = {i: possibilities[i] for i in possibilities if i != "J"}
    counts_no_j = sorted(list(pos_no_j.values()), reverse=True)
    counts_no_j[0] += possibilities["J"]

    if counts_no_j[0] == 5:
        return "five of a kind"
    elif counts_no_j[0] == 4:
        return "four of a kind"
    elif counts_no_j[0] == 3 and counts_no_j[1] == 2:
        return "full house"
    elif counts_no_j[0] == 3:
        return "three of a kind"
    elif counts_no_j[0] == 2 and counts_no_j[1] == 2:
        return "two pairs"
    elif counts_no_j[0] == 2:
        return "one pair"
    else:
        return "nothing"

if __name__ == "__main__":
    # with open('example.txt', 'r') as file:
    with open('input.txt', 'r') as file:
        # Read the lines
        lines = file.readlines()
        lines = [line.strip() for line in lines]

    cards = ['2','3','4','5','6','7','8','9','T','J','Q','K','A']

    hand_bids = []
    for line in lines:
        hand =  [char for char in line.split()[0]]
        bid = int(line.split()[1])

        five = 0
        four = 0
        three = 0
        two = 0
        one = 0

        for card in cards:
            if hand.count(card) == 5:
                five += 1
            elif hand.count(card) == 4:
                four += 1
            elif hand.count(card) == 3:
                three += 1
            elif hand.count(card) == 2:
                two += 1
            elif hand.count(card) == 1:
                one += 1
        if five == 1:
            hand_type = "five of a kind"
        elif four == 1:
            hand_type = "four of a kind"
        elif three == 1 and two == 1:
            hand_type = "full house"
        elif three == 1:
            hand_type = "three of a kind"
        elif two == 2:
            hand_type = "two pairs"
        elif two == 1:
            hand_type = "one pair"
        else:
            hand_type = "nothing"

        hand_bids.append((hand, bid, hand_type))

    winnings = calc_winings(hand_bids, cards)
    print("Part 1: ", winnings) # should be 250058342.0


    cards = ['J','2','3','4','5','6','7','8','9','T','Q','K','A']

    hand_bids = []
    for line in lines:
        hand =  [char for char in line.split()[0]]
        bid = int(line.split()[1])

        five = 0
        four = 0
        three = 0
        two = 0
        one = 0

        for card in cards[1:]:
            if hand.count(card) == 5:
                five += 1
            elif hand.count(card) == 4:
                four += 1
            elif hand.count(card) == 3:
                three += 1
            elif hand.count(card) == 2:
                two += 1
            elif hand.count(card) == 1:
                one += 1
        jokers = hand.count('J')
        if five == 1 or (four == 1 and jokers == 1) or (three == 1 and jokers == 2) or (two == 1 and jokers == 3) or (one == 1 and jokers == 4) or jokers == 5:
            hand_type = "five of a kind"
        elif four == 1 or (three == 1 and jokers == 1) or (two == 1 and jokers == 2) or jokers == 3:
            hand_type = "four of a kind"
        elif (three == 1 and two == 1) or (two == 2 and jokers == 1):
            hand_type = "full house"
        elif three == 1 or (two == 1 and jokers == 1) or (jokers == 2):
            hand_type = "three of a kind"
        elif two == 2:
            hand_type = "two pairs"
        elif two == 1 or jokers == 1:
            hand_type = "one pair"
        else:
            hand_type = "nothing"

        keegan_hand_type = hand_type_2(hand)
        if keegan_hand_type != hand_type:
            print(hand, hand_type, keegan_hand_type)
            exit()

        hand_bids.append((hand, bid, hand_type))
    print(hand_bids)
    winnings = calc_winings(hand_bids, cards)
    print("Part 2: ", winnings) # should be 250506580

    # winnings = calc_winings(
    #     [
    #         (['5', '5', '5', '3', 'K'], 1, 'three of a kind'),
    #         (['5', '5', 'J', 'K', '5'], 2, 'three of a kind')
    #     ],
    #     cards
    # )
    # print("test1: ", winnings) # should be 6")
    # winnings = calc_winings(
    #     [
    #         (['5', '5', '5', '3', 'K'], 1, 'three of a kind'),
    #         (['5', '5', 'J', 'K', '5'], 2, 'three of a kind')
    #     ],
    #     ['2','3','4','5','6','7','8','9','T','J','Q','K','A']
    # )
    # print("test2: ", winnings) # should be 6")







