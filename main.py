from game_logic.game import *

if __name__ == "__main__":
    satrt = init_game()
    while satrt["player_1"]["hand"] and satrt["player_2"]["hand"]:
        play_round(satrt["player_1"], satrt["player_2"])
        
    if len(satrt["player_1"]["won_pile"]) > len(satrt["player_2"]["won_pile"]):
        print(f"Game Winner is:  !!!! {satrt['player_1']["name"]} !!!!")
    elif len(satrt["player_1"]["won_pile"]) < len(satrt["player_2"]["won_pile"]):
        print(f"Game Winner is:  !!!! {satrt['player_2']["name"]} !!!!")
    else:
        print("Win Win")