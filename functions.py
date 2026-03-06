current: str = "X"
moves_journal: list = []
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
def create_board(): #🧊
    board: list = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    return board
# '''
# Returns a new empty board
# Example board format: ['1','2','3','4','5','6','7','8','9']'''
#
#
def print_board(board) : #🖼️
    for i in range(0, 9, 3):
        print(" " + board[i] + " | " + board[i + 1] + " | " + board[i + 2])
        if i < 6:
            print("---+---+---")
# '''
# Print the board like this:
#  1 | 2 | 3
# ---+---+---
#  4 | 5 | 6
# ---+---+---
#  7 | 8 | 9'''
#
#
def get_move(moves_journal) :#🎮
    while True:
        move = input("Choose a tile: ")
        if move.strip().isdigit() == False  :
            print("Invalid input")
            continue
        move = int(move.strip())
        if move > 9 or move < 1 :
            print("Invalid input")
            continue
        if move in moves_journal:
            print("Invalid input")
            continue
        moves_journal.append(move)
        return move




# '''
# Ask the player to choose a spot
#
# must handle:
# not a number
# number not in 1–9
# spot already taken'''
#
def make_move(board, move, current) : #🧲
    if current == "X":
        board[move - 1] = "X"
    else:
        board[move - 1] = "O"
    return board
# '''
# Updates the board'''
#
def check_winner(board): #🏆
    for i in range(0, 9, 3):
        if board[i] == board[i + 1] == board[i + 2]:
            return True
    for i in range(0, 3):
        if board[i] == board[i +3] == board[i + 6]:
            return True
    if board[0] == board[4] == board[8] or board[2] == board[4] == board[6]:
        return True
    return False
# '''
# Returns True if the symbol has 3 in a row'''
#
def is_tie(moves_journal): #🤝
    if len(moves_journal) == 9:
        return True
    return False

# '''
# Returns True if no spots left and no winner'''
#
def switch_player(current): #🔁
    if current == "X":
        return "O"
    else:
        return "X"
# '''
# Switch between players'''
#
def play_game():  #🚀
    print("Welcome to Tic Tac Toe!")
    while True:
        moves_journal: list = []
        board = create_board()
        current = "X"
        while True:
            print_board(board)
            move = get_move(moves_journal)
            make_move(board, move, current)
            if check_winner(board):
                print_board(board)
                print("Congratulations! You won!")
                break
            if is_tie(moves_journal):
                print("Tie!\n")
                break
            current = switch_player(current)


# '''
# Runs the whole game'''
