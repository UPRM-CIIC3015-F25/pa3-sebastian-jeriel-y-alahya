from Cards.Card import Card, Rank

# TODO (TASK 3): Implement a function that evaluates a player's poker hand.
#   Loop through all cards in the given 'hand' list and collect their ranks and suits.
#   Use a dictionary to count how many times each rank appears to detect pairs, three of a kind, or four of a kind.
#   Sort these counts from largest to smallest. Use another dictionary to count how many times each suit appears to check
#   for a flush (5 or more cards of the same suit). Remove duplicate ranks and sort them to detect a
#   straight (5 cards in a row). Remember that the Ace (rank 14) can also count as 1 when checking for a straight.
#   If both a straight and a flush occur in the same suit, return "Straight Flush". Otherwise, use the rank counts
#   and flags to determine if the hand is: "Four of a Kind", "Full House", "Flush", "Straight", "Three of a Kind",
#   "Two Pair", "One Pair", or "High Card". Return a string with the correct hand type at the end.
def evaluate_hand(hand: list[Card]):

    rank_counts = {}
    suit_counts = {}

    for card in hand:
        rank_counts[card.rank.value] = rank_counts.get(card.rank.value, 0) + 1
        suit_counts[card.suit] = suit_counts.get(card.suit, 0) + 1


    flush_suit = None
    for suit, count in suit_counts.items():
        if count >= 5:
            flush_suit = suit
            break


    ranks = sorted(set(card.rank.value for card in hand))


    if 14 in ranks:
        ranks.append(1)
        ranks = sorted(set(ranks))

    straight_found = False
    straight_high = None


    for i in range(len(ranks) - 4):
        if (ranks[i] + 1 == ranks[i+1] and
            ranks[i] + 2 == ranks[i+2] and
            ranks[i] + 3 == ranks[i+3] and
            ranks[i] + 4 == ranks[i+4]):
            straight_found = True
            straight_high = ranks[i+4]
            break


    if flush_suit is not None:
        flush_cards = sorted(
            [card.rank.value for card in hand if card.suit == flush_suit]
        )


        flush_unique = sorted(set(flush_cards))
        if 14 in flush_unique:
            flush_unique.append(1)
            flush_unique = sorted(set(flush_unique))

        for i in range(len(flush_unique) - 4):
            if (flush_unique[i] + 1 == flush_unique[i+1] and
                flush_unique[i] + 2 == flush_unique[i+2] and
                flush_unique[i] + 3 == flush_unique[i+3] and
                flush_unique[i] + 4 == flush_unique[i+4]):
                return "Straight Flush"


    counts_sorted = sorted(rank_counts.values(), reverse=True)


    if counts_sorted[0] == 4:
        return "Four of a Kind"


    if counts_sorted[0] == 3 and counts_sorted[1] >= 2:
        return "Full House"


    if flush_suit is not None:
        return "Flush"


    if straight_found:
        return "Straight"


    if counts_sorted[0] == 3:
        return "Three of a Kind"

    if 2 in counts_sorted:
        if counts_sorted.count(2) == 2:
            return "Two Pair"
        else:
            return "One Pair"


    if counts_sorted[0] == 2:
        return "One Pair"


    return "High Card"