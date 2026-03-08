# '''
# 🗺️ Game plan (build it like a boss)
# Phase 1 — Board basics 🧱
# Create the board data
# Print it nicely
#
# Phase 2 — Player turns 🎯
# Ask for input
# Validate input
# Place the symbol
#
# Phase 3 — Win / tie detection 🏁
# Check rows, columns, diagonals
# Detect tie
#
# Phase 4 — Replay + polish ✨
# Ask “Play again?”
# Add fun messages
# Optional: scoreboard
# '''
#
import random
import time


def create_board(): #🧊
    board = ['1','2','3','4','5','6','7','8','9']
    return board
# '''
# Returns a new empty board
# Example board format: ['1','2','3','4','5','6','7','8','9']'''
#
#
def print_board(board) : #🖼️
    for row in range(0, 9, 3):
        print(f"     {board[row]}   | {board[row + 1]}   | {board[row + 2]}" )
        if row < 6:
            print("    -----+-----+-----")

# '''
# Print the board like this:
#  1 | 2 | 3
# ---+---+---
#  4 | 5 | 6
# ---+---+---
#  7 | 8 | 9'''
#
#
def get_move(board) :#🎮
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
# '''
# Ask the player to choose a spot
#
# must handle:
# not a number
# number not in 1–9
# spot already taken'''
#
def make_move(board, position, current) : #🧲
    board[position - 1] = current
    return board
# '''
# Updates the board'''
#
def check_winner(board, current): #🏆
    win_options: list = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8], # Row
        [0, 3, 6], [1, 4, 7], [2, 5, 8], # Column
        [0, 4, 8], [2, 4, 6]             # Diagonal
    ]
    for combo in win_options:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] == current:
            return True
    return False
# '''
# Returns True if the symbol has 3 in a row'''
#
def is_tie(board): #🤝
    return not any(tile.isdigit() for tile in board)
# '''
# Returns True if no spots left and no winner'''
#
def switch_player(current): #🔁
    if current == "❌":
        return "⭕"
    else:
        return "❌"
# '''
# Switch between players'''
#
def play_game_PVP(): #🚀
    while True:
        current = "❌"
        board = create_board()
        while True:
            print_board(board)
            position = get_move(board)
            if position == "reset":
                break
            board = make_move(board, position, current)
            if check_winner(board, current):
                break
            elif is_tie(board):
                break
            else:
                current = switch_player(current)

def choose_a_symbol_for_PVC():
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

def pc_move(board):
    while True:
        move = random.randint(1, 9)
        if board[move - 1].isdigit() == False:
            continue
        else:
            return move


def play_game_PVC():
    while True:
        current = "❌"
        board = create_board()
        player = choose_a_symbol_for_PVC()
        while True:
            if player == current:
                print_board(board)
                position = get_move(board)
                if position == "reset":
                    break
                board = make_move(board, position, current)
                if check_winner(board, current):
                    print_board(board)
                    print("You win!")
                    break
                if is_tie(board):
                    print_board(board)
                    print("Tie!")
                    break
                current = switch_player(current)
                print_board(board)
                time.sleep(3)
                position = pc_move(board)
                board = make_move(board, position, current)
                if check_winner(board, current):
                    print_board(board)
                    print("Comp wins")
                    break
                current = switch_player(current)
                continue
            else:
                time.sleep(3)
                position = pc_move(board)
                board = make_move(board, position, current)
                if check_winner(board, current):
                    print_board(board)
                    print("Comp wins")
                    break
                if is_tie(board):
                    print_board(board)
                    print("Tie!")
                    break
                current = switch_player(current)
                print_board(board)
                position = get_move(board)
                if position == "reset":
                    break
                board = make_move(board, position, current)
                if check_winner(board, current):
                    print_board(board)
                    print("You win!")
                    break
                current = switch_player(current)







# '''
# Runs the whole game''''''
# 🗺️ Game plan (build it like a boss)
# Phase 1 — Board basics 🧱
# Create the board data
# Print it nicely
#
# Phase 2 — Player turns 🎯
# Ask for input
# Validate input
# Place the symbol
#
# Phase 3 — Win / tie detection 🏁
# Check rows, columns, diagonals
# Detect tie
#
# Phase 4 — Replay + polish ✨
# Ask “Play again?”
# Add fun messages
# Optional: scoreboard
# '''
#
# def create_board(): #🧊
# '''
# Returns a new empty board
# Example board format: ['1','2','3','4','5','6','7','8','9']'''
#
#
# def print_board(board) : #🖼️
# '''
# Print the board like this:
#  1 | 2 | 3
# ---+---+---
#  4 | 5 | 6
# ---+---+---
#  7 | 8 | 9'''
#
#
# def get_move(player, board) :#🎮
# '''
# Ask the player to choose a spot
#
# must handle:
# not a number
# number not in 1–9
# spot already taken'''
#
# def make_move(board, position, symbol) : #🧲
# '''
# Updates the board'''
#
# def check_winner(board, symbol): #🏆
# '''
# Returns True if the symbol has 3 in a row'''
#
# def is_tie(board): #🤝
# '''
# Returns True if no spots left and no winner'''
#
# def switch_player(current): #🔁
# '''
# Switch between players'''
#
# def play_game(): #🚀
# '''
# Runs the whole game'''