from utils.deck import shuffle, create_deck

def create_player(name:str = "AI") -> dict:
    player = {}
    player["name"] = name
    player["hand"] = []
    player["won_pile"] = []

    return player


def init_game() -> dict:
    game_dict = {}
    player_1 = create_player("dani")
    player_2 = create_player()
    pack_card = shuffle(create_deck())    

    player_1["hand"] = pack_card[:len(pack_card) // 2]
    player_2["hand"] = pack_card[len(pack_card) // 2:]

    game_dict["deck"] = pack_card
    game_dict["player_1"] = player_1
    game_dict["player_2"] = player_2

    return game_dict

    
def play_round(p1:dict,p2:dict):
    pass



