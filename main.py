import functions


while True:
    game_mode = functions.main_menu()
    if game_mode == "1":
        functions.play_game_PVP()
        continue
    elif game_mode == "2":
        functions.play_game_PVC()
        continue
    else:
        print("Thank you for playing!")
        break
