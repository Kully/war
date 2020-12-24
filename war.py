MAX_ITERATIONS = 40000

INT_HEX_LOOKUP = {
    0: "0",
    1: "1",
    2: "2",
    3: "3",
    4: "4",
    5: "5",
    6: "6",
    7: "7",
    8: "8",
    9: "9",
    10: "a",
    11: "b",
    12: "c",
}

HEX_INT_LOOKUP = {
    v:k for v,k in zip(INT_HEX_LOOKUP.values(), INT_HEX_LOOKUP.keys())
}


def make_deck():
    """Generate a 52-card deck of integers."""
    deck = []
    for suit in range(4):
        deck += [i for i in range(13)]
    return sorted(deck)


def serialize(deck_array):
    """
    Convert an array of cards into a string.
    """
    output = ""
    for card in deck_array:
        output += INT_HEX_LOOKUP[card]
    return output


def deserialize(deck_string):
    """
    Convert a string deck to an array.
    """
    output = []
    for char in deck_string:
        output.append(HEX_INT_LOOKUP[char])
    return output


def make_uid(deck_one, deck_two):
    return ":".join([serialize(deck_one), serialize(deck_two)])


def war_turn_states(deck_one, deck_two, max_iterations, debug=False):
    """
    Plays 'The Game of War' and returns a list of all
    the game states with length up to `max_iterations`.
    
    Each string in the returned list is a serialized code
    that represents the cards in player one's deck and
    the cards in player two's deck.
    
    The string, which we name a uid (unique identifier)
    has the form: "hhhhhhhh:hhhhhhhh" where each `h` is
    from the set {0,1,2,3,4,5,6,7,8,9,a,b,c}.
    
    """
    bin_of_cards = []
    turn_states = []
    iteration = 0
    while (iteration <= MAX_ITERATIONS and len(deck_one) != 0 and len(deck_two) != 0):
        # if len(deck_one) + len(deck_two) == 52:
        #     state = make_uid(deck_one, deck_two)
        #     turn_states.append(state)

        if debug:
            print(f"iter [{str(iteration).zfill(2)}]")
            print(f"  deck_one len: {len(deck_one)}")
            print(f"  deck_two len: {len(deck_two)}")
            print(f"  bin_of_cards len: {len(bin_of_cards)}")
            print(f"  Assertion: {len(bin_of_cards) + len(deck_one) + len(deck_two) == 52}")
            print("")

        if deck_one[0] == deck_two[0]:
            for _ in range(3):
                if len(deck_one) > 0:
                    bin_of_cards.append(deck_one.pop(0))
                if len(deck_two) > 0:
                    bin_of_cards.append(deck_two.pop(0))
        elif deck_one[0] > deck_two[0]:
            bin_of_cards.append(deck_one.pop(0))
            bin_of_cards.append(deck_two.pop(0))
            deck_one += bin_of_cards
            bin_of_cards = []

        elif deck_one[0] < deck_two[0]:
            bin_of_cards.append(deck_two.pop(0))
            bin_of_cards.append(deck_one.pop(0))
            deck_two += bin_of_cards
            bin_of_cards = []


        if len(deck_one) + len(deck_two) == 52:
            state = make_uid(deck_one, deck_two)
            turn_states.append(state)

        iteration += 1
    return turn_states
