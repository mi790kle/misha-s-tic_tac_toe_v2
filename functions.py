
import random
import time
board: list = []
current: str = ""
position: int = 0
player: str = ""
game_mode: str = ""

def main_menu() -> str:
    """Main menu of the game, user chooses a game mode (PVP or PVC) or exits the game
    The function asks for input to make a choice, validates and returns it"""
    print("-" * 30)
    print("Welcome to the great TIC TAC TOE tournament!")
    print("❌ ⚔️ ⭕")
    print("-" * 30)
    print("If you wish to restart the game type [restart] or [r], but your scores will be set to 0")
    print("-" * 30)
    while True:
        print(f"Please choose the game mode:")
        print("1 - PVP")
        print("2 - PVC")
        print("3 - close the game")
        game_mode = input()
        if game_mode != "1" and game_mode != "2" and game_mode != "3":
            print("Please make a valid choice.")
            continue
        return game_mode

def create_board() -> list: #🧊
    """Creates a bord as a list and returns it"""
    board = ['1','2','3','4','5','6','7','8','9']
    return board

def print_board(board: list) -> None: #🖼️
    """Prints the board in a native gaming way"""
    for row in range(0, 9, 3):
        print(f"{board[row]} | {board[row + 1]} | {board[row + 2]}" )
        if row < 6:
            print("---+---+---")


def get_move(board: list) -> str | int:#🎮
    """Asks for an input to make a move and validates it, also allows to reset the game or access the main menu"""
    print("if you want to make a move enter a number between 1 and 9, and if you wish to restart enter [r] or [reset]")
    while True:
        move = input ("Enter your move: ")
        if move.lower() == "r" or move.lower() == "reset":
            return "reset"
        if move.strip().isdigit() == False:
            print("Please enter a valid move.")
            continue
        if int(move.strip()) > 9 or int(move.strip()) < 1:
            print("Please enter a valid move.")
            continue
        if board[int(move.strip()) - 1].isdigit() == False:
            print("The tile is already taken, choose another one.")
            continue
        return int(move.strip())

def make_move(board: list, position: int, current: str) -> list: #🧲
    """Executes the move and returns the changed board"""
    board[position - 1] = current
    return board

def check_winner(board: list, current: str) -> bool:#🏆
    """Checks if there is a winner at this turn"""
    WIN_OPTIONS: list = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # Row
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # Column
        [0, 4, 8], [2, 4, 6]             # Diagonal
    ]
    for combo in WIN_OPTIONS:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == current:
            board[combo[0]] += "🏆"
            board[combo[1]] += "🏆"
            board[combo[2]] += "🏆"
            return True
    return False


def PVC_scores(player_score: int, computer_score: int, player: str, current: str) -> int:
    """Updates the score for PVC mode"""
    if player == current:
        player_score += 1
        return player_score
    else:
        computer_score += 1
        return computer_score

def is_tie(board: list) -> bool: #🤝
    """Checks if there is a tie"""
    return not any(tile.isdigit() for tile in board)

def switch_player(current: str) -> str: #🔁
    """switches the current player"""
    if current == "❌":
        return "⭕"
    else:
        return "❌"

def play_game_PVP() -> None: #🚀
    """Main PVP loop, includes all the logic of the game, uses all the other related functions"""
    x_score: int = 0
    o_score: int = 0
    draws: int = 0
    while True:
        current = "❌"
        board = create_board()
        while True:
            print(f"It's {current}'s turn, make a move!")
            print_board(board)
            position = get_move(board)
            if position == "reset":
                x_score = 0
                o_score = 0
                draws = 0
                break
            board = make_move(board, position, current)
            if check_winner(board, current):
                print("We have a winner!")
                print_board(board)
                if current == "❌":
                    x_score += 1
                else:
                    o_score += 1
                print("-" * 11)
                print(f"❌: {x_score}")
                print(f"⭕: {o_score}")
                print(f"Draws: {draws}")
                print("Do you want to go for another round?")
                while True:
                    keep_playing: str = input("1 - Yes     2 - No")
                    keep_playing = keep_playing.strip()
                    if keep_playing.isdigit():
                        if keep_playing != "1" and keep_playing != "2":
                            print("Please enter 1 to continue or 2 to get to the main menu.")
                            continue
                        if keep_playing == "1":
                            break
                        if keep_playing == "2":
                            return
                    else:
                        print("Please enter 1 to continue or 2 to get to the main menu.")
                        continue
                break
            elif is_tie(board):
                print("Tie!")
                draws += 1
                print_board(board)
                print("-" * 11)
                print(f"❌: {x_score}")
                print(f"⭕: {o_score}")
                print(f"Draws: {draws}")
                print("Do you want to go for another round?")
                while True:
                    keep_playing: str = input("1 - Yes     2 - No")
                    keep_playing = keep_playing.strip()
                    if keep_playing.isdigit():
                        if keep_playing != "1" and keep_playing != "2":
                            print("Please enter 1 to continue or 2 to get to the main menu.")
                            continue
                        if keep_playing == "1":
                            break
                        if keep_playing == "2":
                            return
                    else:
                        print("Please enter 1 to continue or 2 to get to the main menu.")
                        continue
                break
            else:
                current = switch_player(current)

def choose_a_symbol_for_PVC() -> str:
    """Lets the player choose a symbol in PVC mode"""
    while True:
        print("You have 2 symbols to choose, for playing as ❌ press 1, for playing as ⭕ press 2 ")
        symbol = input("Choose a symbol: ")
        if symbol == "1":
            symbol = "❌"
            return symbol
        elif symbol == "2":
            symbol = "⭕"
            return symbol
        else:
            print("Please enter a valid choice.")
            continue

def pc_move(board: list) -> int:
    """Gets a random move for computer in PVC mode"""
    while True:
        move = random.randint(1, 9)
        if board[move - 1].isdigit() == False:
            continue
        else:
            return move


def play_game_PVC() -> None:
    """Main PVC loop, includes all the logic of the game, uses all the other related functions"""
    player_score: int = 0
    computer_score: int = 0
    draws: int = 0
    while True:
        current = "❌"
        board = create_board()
        player = choose_a_symbol_for_PVC()
        while True:
            if player == current:
                print_board(board)
                position = get_move(board)
                if position == "reset":
                    player_score = 0
                    computer_score = 0
                    draws = 0
                    break
                board = make_move(board, position, current)
                if check_winner(board, current):
                    print("You win!")
                    print_board(board)
                    player_score += 1
                    print(f"Player: {player_score}")
                    print(f"Computer: {computer_score}")
                    print(f"Draws: {draws}")
                    print("Do you want to go for another round?")
                    while True:
                        keep_playing: str = input("1 - Yes     2 - No")
                        keep_playing = keep_playing.strip()
                        if keep_playing.isdigit():
                            if keep_playing != "1" and keep_playing != "2":
                                print("Please enter 1 to continue or 2 to get to the main menu.")
                                continue
                            if keep_playing == "1":
                                break
                            if keep_playing == "2":
                                return
                        else:
                            print("Please enter 1 to continue or 2 to get to the main menu.")
                            continue
                    break
                if is_tie(board):
                    print("Tie!")
                    print_board(board)
                    draws += 1
                    print(f"Player: {player_score}")
                    print(f"Computer: {computer_score}")
                    print(f"Draws: {draws}")
                    print("Do you want to go for another round?")
                    while True:
                        keep_playing: str = input("1 - Yes     2 - No")
                        keep_playing = keep_playing.strip()
                        if keep_playing.isdigit():
                            if keep_playing != "1" and keep_playing != "2":
                                print("Please enter 1 to continue or 2 to get to the main menu.")
                                continue
                            if keep_playing == "1":
                                break
                            if keep_playing == "2":
                                return
                        else:
                            print("Please enter 1 to continue or 2 to get to the main menu.")
                            continue
                    break
                current = switch_player(current)
                print_board(board)
                print("Computer is making his move...")
                time.sleep(1.5)
                position = pc_move(board)
                board = make_move(board, position, current)
                if check_winner(board, current):
                    print("Comp wins")
                    print_board(board)
                    computer_score += 1
                    print(f"Player: {player_score}")
                    print(f"Computer: {computer_score}")
                    print(f"Draws: {draws}")
                    print("Do you want to go for another round?")
                    while True:
                        keep_playing: str = input("1 - Yes     2 - No")
                        keep_playing = keep_playing.strip()
                        if keep_playing.isdigit():
                            if keep_playing != "1" and keep_playing != "2":
                                print("Please enter 1 to continue or 2 to get to the main menu.")
                                continue
                            if keep_playing == "1":
                                break
                            if keep_playing == "2":
                                return
                        else:
                            print("Please enter 1 to continue or 2 to get to the main menu.")
                            continue
                    break
                current = switch_player(current)
                continue
            else:
                print("Computer is making his move...")
                time.sleep(1.5)
                position = pc_move(board)
                board = make_move(board, position, current)
                if check_winner(board, current):
                    print("Comp wins")
                    print_board(board)
                    computer_score += 1
                    print(f"Player: {player_score}")
                    print(f"Computer: {computer_score}")
                    print(f"Draws: {draws}")
                    print("Do you want to go for another round?")
                    while True:
                        keep_playing: str = input("1 - Yes     2 - No")
                        keep_playing = keep_playing.strip()
                        if keep_playing.isdigit():
                            if keep_playing != "1" and keep_playing != "2":
                                print("Please enter 1 to continue or 2 to get to the main menu.")
                                continue
                            if keep_playing == "1":
                                break
                            if keep_playing == "2":
                                return
                        else:
                            print("Please enter 1 to continue or 2 to get to the main menu.")
                            continue
                    break
                if is_tie(board):
                    print("Tie!")
                    print_board(board)
                    draws += 1
                    print(f"Player: {player_score}")
                    print(f"Computer: {computer_score}")
                    print(f"Draws: {draws}")
                    print("Do you want to go for another round?")
                    while True:
                        keep_playing: str = input("1 - Yes     2 - No")
                        keep_playing = keep_playing.strip()
                        if keep_playing.isdigit():
                            if keep_playing != "1" and keep_playing != "2":
                                print("Please enter 1 to continue or 2 to get to the main menu.")
                                continue
                            if keep_playing == "1":
                                break
                            if keep_playing == "2":
                                return
                        else:
                            print("Please enter 1 to continue or 2 to get to the main menu.")
                            continue
                    break
                current = switch_player(current)
                print_board(board)
                position = get_move(board)
                if position == "reset":
                    player_score = 0
                    computer_score = 0
                    draws = 0
                    break
                board = make_move(board, position, current)
                if check_winner(board, current):
                    print("You win!")
                    print_board(board)
                    player_score += 1
                    print(f"Player: {player_score}")
                    print(f"Computer: {computer_score}")
                    print(f"Draws: {draws}")
                    print("Do you want to go for another round?")
                    while True:
                        keep_playing: str = input("1 - Yes     2 - No")
                        keep_playing = keep_playing.strip()
                        if keep_playing.isdigit():
                            if keep_playing != "1" and keep_playing != "2":
                                print("Please enter 1 to continue or 2 to get to the main menu.")
                                continue
                            if keep_playing == "1":
                                break
                            if keep_playing == "2":
                                return
                        else:
                            print("Please enter 1 to continue or 2 to get to the main menu.")
                            continue
                    break
                current = switch_player(current)