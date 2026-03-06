board = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
for i in range(0, 9, 3):
    print(" " + board[i] + " | " + board[i + 1] + " | " + board[i + 2])
    if i < 6:
        print("---+---+---")
board[5] = 'X'
for i in range(0, 9, 3):
    print(" " + board[i] + " | " + board[i + 1] + " | " + board[i + 2])
    if i < 6:
        print("---+---+---")