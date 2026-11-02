# Minimax Algorithm

def minimax(score, is_max):
    if score == 0:
        return 0

    if is_max:
        return max(score, -score)
    else:
        return min(score, -score)


print("Tic-Tac-Toe Minimax Agent")

score = int(input("Enter game score (-1, 0, or 1): "))

if score == 1:
    print("Agent Wins!")

elif score == -1:
    print("Opponent Wins!")

else:
    print("Game is draw!")