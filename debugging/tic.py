def print_board(board):
    """
    Affiche le tableau de jeu.
    Chaque ligne du tableau est imprimée avec des séparateurs et une ligne de séparation est ajoutée.
    """
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    """
    Vérifie si un joueur a gagné. 
    Retourne True si un gagnant est trouvé, sinon False.
    """
    # Vérification des lignes
    for row in board:
        if row.count(row[0]) == len(row) and row[0] != " ":
            return True

    # Vérification des colonnes
    for col in range(len(board[0])):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != " ":
            return True

    # Vérification des diagonales
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != " ":
        return True

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != " ":
        return True

    return False

def tic_tac_toe():
    """
    Fonction principale du jeu de Tic Tac Toe. Gère le flux du jeu, l'alternance des joueurs, et l'affichage du tableau.
    """
    board = [[" "]*3 for _ in range(3)]  # Initialisation du tableau vide
    player = "X"  # Le joueur qui commence est "X"
    while not check_winner(board):
        print_board(board)
        try:
            # Demande à l'utilisateur d'entrer les coordonnées de la ligne et de la colonne
            row = int(input("Enter row (0, 1, or 2) for player " + player + ": "))
            col = int(input("Enter column (0, 1, or 2) for player " + player + ": "))
            
            # Vérification que les coordonnées sont valides
            if row not in range(3) or col not in range(3):
                print("Invalid input! Row and column must be between 0 and 2.")
                continue

            # Vérifie si la case est déjà occupée
            if board[row][col] == " ":
                board[row][col] = player
                if player == "X":
                    player = "O"
                else:
                    player = "X"
            else:
                print("That spot is already taken! Try again.")
        except ValueError:
            print("Invalid input! Please enter numeric values for row and column.")

    print_board(board)
    print("Player " + ("O" if player == "X" else "X") + " wins!")

# Appel à la fonction pour démarrer le jeu
tic_tac_toe()
