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

    
def play_round(p1:dict,p2:dict) -> None:

    bucket = []

    player_1 = p1["hand"].pop(0)
    player_2 = p2["hand"].pop(0)

    if player_1["value"] > player_2["value"]:
        p1["won_pile"].append(player_1)
        p1["won_pile"].append(player_2)
        if bucket:
            p1["won_pile"].extend(bucket)
        print(f"{p1["name"]} Win this round")

    elif player_1["value"] < player_2["value"]:
        p2["won_pile"].append(player_1)
        p2["won_pile"].append(player_2)
        if bucket:
            p2["won_pile"].extend(bucket)
        print(f"{p2["name"]} Win this round")

    else:
        if len(p1["hand"]) > 3 and len (p2["hand"]) > 3:
            print("! W  A R !")
            bucket = []
            for i in range(3):
                player_1 = p1["hand"].pop(0)
                player_2 = p2["hand"].pop(0)
                bucket.append(player_1)
                bucket.append(player_2)
            play_round(p1, p2)