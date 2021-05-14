def sum_cards(lst):
    tens = 'KQJ10'
    ace = 'A'
    nums = '23456789'
    sum = 0

    hand1 = {}
    hand2 = ''
    for card in lst:
        if card is ace:
            hand2 += card
    for card in lst:
        if (card in tens or card in nums) and card not in hand1.keys():
            hand1[card] = 1
        if (card in tens or card in nums) and card in hand1.keys():
            hand1[card] = +1
    #  counting normal cards:
    for each in hand1.keys():

        if each in tens:
            sum += 10 * int(hand1[each])

        if each in nums:
            sum += int(each) * int(hand1[each])


        # if only 1 Ace
    if len(hand2) == 1:
        if sum + 11 <= 21:
            sum += 11
        else:
            sum += 1

    if len(hand2) > 1:
            # if more than 1 Ace but > 21 even if all Aces = 1
        if sum + len(hand2) > 21:
            sum += len(hand2)
            # if winning is possible
        if sum + len(hand2) <= 21:
                # if one can be 11 and other 1 to win
            if sum + 11 + len(hand2) - 1 <= 21:
                sum += 11 + len(hand2) - 1
            elif sum + len(hand2) <= 21:
                sum += len(hand2)


    return sum


def blackjack_hand_greater_than(hand_1, hand_2):

    if sum_cards(hand_1) > 21:
        return False
    if sum_cards(hand_1) > sum_cards(hand_2):
        return True
    if sum_cards(hand_2) > 21:
        return True
    else:
        return False



print(sum_cards(['A', '4', '4', '7']))

print(sum_cards(['2', 'A', 'A', '6']))

print(blackjack_hand_greater_than(hand_2=['A', '4', '4', '7'],  hand_1=['2',
                                                                        '8',
                                                                        '3']))
