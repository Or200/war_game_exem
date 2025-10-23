import random

def create_card(rank:str,suite:str) -> dict:
    card = {}
    valid_card = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "A", "J", "Q", "K"]
    valid_suite = ["H", "C", "D", "S"]
    rank_str = rank
    if rank in valid_card and suite in valid_suite:
        if rank in ["A", "J", "Q", "K"]:
            if rank == "A":
                rank = "14"
            elif rank == "J":
                rank = "11"
            elif rank == "Q":
                rank = "12"
            else:
                rank = "13"
        card["rank"] = rank_str
        card["suite"] = suite
        card["value"] = int(rank)
    else:
        print("Card not created - write valid values")
    return card


def compare_cards(p1_card:dict, p2_card:dict) -> str:
    p1 = p1_card.get("value")
    p2 = p2_card.get("value")
    if p1 == p2:
        return "WAR"
    elif p1 > p2:
        return "p1"
    else:
        return "p2"


def create_deck() -> list[dict]:
    pack_of_card = []
    cards_rank = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
    cards_suite = ["H", "C", "D", "S"]
    for card_rank in cards_rank:
        for card_suite in cards_suite:
            pack_of_card.append(create_card(card_rank, card_suite))
    return pack_of_card


def shuffle(deck:list[dict]) -> list[dict]:
    for shfle in range(1000):
        index1 = random.randint(0, 51)
        index2 = random.randint(0, 51)
        if index1 != index2:
            deck[index1], deck[index2] = deck[index2], deck[index1]
    return deck



