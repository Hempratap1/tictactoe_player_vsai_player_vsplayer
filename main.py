# Initialize the game board
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
    print(f"Player {player}'s turn")

    # Get player input for row and column
    row = int(input("Enter row (0, 1, or 2): "))
    col = int(input("Enter column (0, 1, or 2): "))

    # Check if the chosen cell is empty
    if board[row][col] == " ":
        board[row][col] = player

        # Check for a win
        # Check rows, columns, and diagonals for a complete line of player's marks
        for i in range(3):
            if all(board[i][j] == player for j in range(3)) or \
               all(board[j][i] == player for j in range(3)):
                print(f"Player {player} wins!")
                exit()  # Exit the program if there's a win

        if all(board[i][i] == player for i in range(3)) or \
           all(board[i][2 - i] == player for i in range(3)):
            print(f"Player {player} wins!")
            exit()  # Exit the program if there's a win

        # Check for a draw
        if all(cell != " " for row in board for cell in row):
            for row in board:
                print(" | ".join(row))
                print("-" * 9)
            print("It's a draw!")
            exit()  # Exit the program if it's a draw

        # Switch to the other player for the next turn
        current_player = (current_player + 1) % 2
    else:
        print("That position is already taken. Try again.")
