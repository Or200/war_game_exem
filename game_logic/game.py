def create_player(name:str = "AI") -> dict:
    player = {}
    player["name"] = name
    player["hand"] = []
    player["won_pile"] = []

    return player

    



def init_game() -> dict:
    return {}

def play_round(p1:dict,p2:dict):
    pass



print(create_player())
print(create_player("p1"))