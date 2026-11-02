
# Tic-Tac-Toe using Minimax Algorithm

# Create empty board
board = [" " for i in range(9)]


# Check whether a player has won
def check_win(player):

    win_positions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]

    for a, b, c in win_positions:

        if board[a] == board[b] == board[c] == player:
            return True

    return False


# Check whether board is full
def is_full():

    return " " not in board


# Minimax algorithm
def minimax(is_max):

    # Computer wins
    if check_win("O"):
        return 1

    # Human wins
    if check_win("X"):
        return -1

    # Draw
    if is_full():
        return 0

    if is_max:

        best = -1000

        # Computer tries to maximize score
        for i in range(9):

            if board[i] == " ":

                board[i] = "O"

                score = minimax(False)

                # Undo move
                board[i] = " "

                best = max(best, score)

        return best

    else:

        best = 1000

        # Human tries to minimize score
        for i in range(9):

            if board[i] == " ":

                board[i] = "X"

                score = minimax(True)

                # Undo move
                board[i] = " "

                best = min(best, score)

        return best


# Find best move for computer
def best_move():

    best_score = -1000
    move = -1

    for i in range(9):

        if board[i] == " ":

            board[i] = "O"

            score = minimax(False)

            board[i] = " "

            if score > best_score:

                best_score = score
                move = i

    return move


# Display game board
def display_board():

    print()

    for i in range(9):

        print(board[i], end="")

        if i % 3 != 2:
            print(" | ", end="")

        if i % 3 == 2 and i != 8:
            print("\n---------")

    print("\n")


# Main game
print("TIC TAC TOE")
print("You are X, Computer is O.")

while True:

    display_board()

    # Human move
    position = int(input("Enter position (1-9): ")) - 1

    # Check valid position
    if position < 0 or position > 8 or board[position] != " ":

        print("Invalid position!")
        continue

    board[position] = "X"

    # Check human win
    if check_win("X"):

        display_board()
        print("You Win!")
        break

    # Check draw
    if is_full():

        display_board()
        print("Game Draw!")
        break

    # Computer move
    move = best_move()

    board[move] = "O"

    print("Computer selected:", move + 1)

    # Check computer win
    if check_win("O"):

        display_board()
        print("Computer Wins!")
        break

    # Check draw
    if is_full():

        display_board()
        print("Game Draw!")
        break
