# Initialize the game board
import random
import time

board = [[" " for _ in range(3)] for _ in range(3)]
players = ["X", "O"]
current_player = 0

print("Welcome to Tic Tac Toe!")

while True:
    # Display the current state of the board
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

    player = players[current_player]
    print(f"Player {player}'s turn\n")
    if current_player == 1:
        time.sleep(3)

        row = random.randint(0, 2)
        col = random.randint(0, 2)

    else:
        row = int(input("Enter row (0, 1, or 2): "))
        col = int(input("Enter column (0, 1, or 2): "))

    if board[row][col] == " ":
        board[row][col] = player

        for i in range(3):
            if all(board[i][j] == player for j in range(3)) or \
               all(board[j][i] == player for j in range(3)):
                for row in board:
                    print(" | ".join(row))
                    print("-" * 9)
                print(f"Player {player} wins!")
                exit()

        if all(board[i][i] == player for i in range(3)) or \
           all(board[i][2 - i] == player for i in range(3)):
            for row in board:
                print(" | ".join(row))
                print("-" * 9)
            print(f"Player {player} wins!")
            exit()

        if all(cell != " " for row in board for cell in row):
            for row in board:
                print(" | ".join(row))
                print("-" * 9)
            print("It's a draw!")
            exit()

        current_player = (current_player + 1) % 2
    else:
        print("That position is already taken. Try again.")
