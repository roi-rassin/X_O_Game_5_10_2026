def print_board(board):
    """Print the current 3 x 3 game board."""
    for row_number, row in enumerate(board):
        print(" | ".join(row))
        if row_number < 2:
            print("---------")
    print()


def get_move(board, player):
    """Keep asking until the player chooses a valid empty square."""
    while True:
        choice = input(f"Player {player}, choose a square (1-9): ")

        if not choice.isdigit():
            print("Invalid input. Please enter a number from 1 to 9.")
            continue

        square = int(choice)

        if square < 1 or square > 9:
            print("That number is out of range. Please choose from 1 to 9.")
            continue

        row = (square - 1) // 3
        column = (square - 1) % 3

        if board[row][column] != " ":
            print("That square is already taken. Please choose another square.")
            continue

        return row, column


def check_winner(board, player):
    """Return True if the player has three symbols in a row."""
    winning_lines = [
        board[0],
        board[1],
        board[2],
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]],
    ]

    return [player, player, player] in winning_lines

while True:
    board = [
        [" ", " ", " "],
        [" ", " ", " "],
        [" ", " ", " "],
    ]

    print("A new game has started!")
    print_board(board)

    while True:
        # Player X's turn
        row, column = get_move(board, "X")
        board[row][column] = "X"
        print_board(board)

        if check_winner(board, "X"):
            print("Player X wins!")
            break

        empty_square_exists = False
        for board_row in board:
            if " " in board_row:
                empty_square_exists = True
                break

        if not empty_square_exists:
            print("It is a draw!")
            break

        # Player O's turn
        row, column = get_move(board, "O")
        board[row][column] = "O"
        print_board(board)

        if check_winner(board, "O"):
            print("Player O wins!")
            break

    while True:
        play_again = input("Would you like to play again? (yes/no): ").strip().lower()
        if play_again in ("yes", "y"):
            print()
            break
        if play_again in ("no", "n"):
            print("Thanks for playing. Goodbye!")
            break
        print("Invalid input. Please enter yes or no.")

    if play_again in ("no", "n"):
        break