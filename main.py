def print_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 5)
    print("\n")

def check_winner(board, player):
    # Check rows, columns, and diagonals for a win
    for row in board:
        if all(s == player for s in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_full(board):
    return all(all(cell != " " for cell in row) for row in board)

def tic_tac_toe():
    # Initialize the game board
    board = [[" " for _ in range(3)] for _ in range(3)]
    players = ["X", "O"]
    current_player = 0

    print("Bienvenue au Tic Tac Toe!")
    print_board(board)

    while True:
        # Get the current player's move
        print(f"Joueur {players[current_player]}, c'est votre tour.")
        try:
            row = int(input("Entrez la ligne (0, 1 ou 2) : "))
            col = int(input("Entrez la colonne (0, 1 ou 2) : "))
            if board[row][col] != " ":
                print("Cette case est déjà occupée! Réessayez.")
                continue
        except (ValueError, IndexError):
            print("Entrée invalide. Assurez-vous d'entrer 0, 1 ou 2 pour la ligne et la colonne.")
            continue

        # Make the move
        board[row][col] = players[current_player]
        print_board(board)

        # Check if the player has won
        if check_winner(board, players[current_player]):
            print(f"Félicitations, Joueur {players[current_player]} a gagné!")
            break

        # Check for a draw
        if is_full(board):
            print("Match nul!")
            break

        # Switch to the other player
        current_player = 1 - current_player

if __name__ == "__main__":
    tic_tac_toe()
