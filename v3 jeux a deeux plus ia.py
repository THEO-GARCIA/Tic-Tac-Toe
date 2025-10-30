
choix=int(input("vouler vous jouer seul (1) ou a deux (2) : "))
# plateaux de jeu
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

player2= "X"
player = "O"
gagnant = None
game = True

# création du plateau
def printboard(board):
    print()
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])
    print() 

# entrée de la valeur désirée
def playerinput(board):
    chiffre = int(input("Entre un chiffre en 1 et 9: "))
    if chiffre >= 1 and chiffre <= 9 and board[chiffre - 1] == "-":
        board[chiffre - 1] = player
       
    else:
        print("Cette place est déjà prise.")

def playerinput2(board):
    chiffre = int(input("Entre un chiffre en 1 et 9: "))
    if chiffre >= 1 and chiffre <= 9 and board[chiffre - 1] == "-":
        board[chiffre - 1] = player
       
    else:
        print("Cette place est déjà prise.")



# vérif si win ou pas
def win_horizontal(board):
    global gagnant
    if board[0]==board[1]==board[2]and board[0]!= "-":
        gagnant= board[0]
        return True
    elif board[3]==board[4]==board[5]and board[3]!= "-":
        gagnant= board[3]
        return True
    elif board[6]==board[7]==board[8]and board[6]!= "-":
        gagnant= board[6]
        return True

def win_vertical(board):
    global gagnant
    if board[0]==board[3]==board[6]and board[0]!= "-":
        gagnant= board[0]
        return True
    elif board[1]==board[4]==board[7]and board[1]!= "-":
        gagnant= board[1]
        return True
    elif board[2]==board[5]==board[8]and board[2]!= "-":
        gagnant= board[2]
        return True

def win_diag(board):
    global gagnant
    if board[0]==board[4]==board[8]and board[0] != "-":
        gagnant=board[0]
        return True
    elif board[2]==board[4]==board[6]and board[2] != "-":
        gagnant=board[2]
        return True

def verif_gagnant():
    global game
    if win_diag(board) or win_horizontal(board) or win_vertical(board):
        print(f"Le gagnant est {gagnant} !")
        game = False

def verif_nul(board):
    global game
    if "-" not in board and gagnant is None:
        # 'and gagnant is None' pour éviter "match nul" après un coup gagnant
        printboard(board)
        print("Match nul !!!!")
        game=False

def changement():
    global player
    if player == "X":
        player= "O"
    else:
        player="X"


def ia(board):
    global player
    if "-" not in board:
        return  

    
    gagnant_possibles = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],
        [0, 3, 6], [1, 4, 7], [2, 5, 8],
        [0, 4, 8], [2, 4, 6]
    ]

    # Fonction pour trouver un coup gagnant ou bloquant
    def trouver_meilleur_coup(x):
        for combo in gagnant_possibles:
            cases = [board[i] for i in combo]
            if cases.count(x) == 2 and cases.count("-") == 1:
                return combo[cases.index("-")]
        return None

    # L'IA joue uniquement quand c'est son tour
    if player == "X":
        # Étape 1 : jouer pour gagner
        coup = trouver_meilleur_coup("X")
        if coup is not None:
            board[coup] = "X"
            changement()
            return

        # Étape 2 : bloquer le joueur
        coup = trouver_meilleur_coup("O")
        if coup is not None:
            board[coup] = "X"
            changement()
            return

        # Étape 3 : jouer au centre
        if board[4] == "-":
            board[4] = "X"
            changement()
            return

        # Étape 4 : jouer dans un coin
        for i in [0, 2, 6, 8]:
            if board[i] == "-":
                board[i] = "X"
                changement()
                return

        # Étape 5 : sinon jouer n’importe où
        for i in range(9):
            if board[i] == "-":
                board[i] = "X"
                changement()
                return


def boucle_ia():
  while game:
    printboard(board)
    playerinput(board)
    verif_gagnant()
    verif_nul(board)
    if not game:
        break

    changement()
    ia(board)
    verif_gagnant()
    verif_nul(board)
    if not game:
        break






def boucle_adeux():
  while game:
   printboard(board)
   playerinput(board)
   verif_gagnant()
   verif_nul(board)
   if not game:
         break
   changement()
   printboard(board)
    
   playerinput2(board)
   verif_gagnant()
   verif_nul(board)

   if not game:
      # stop si le jeu est fini
        break
   changement()
    
        
    
         
     
     
if choix==1:
    boucle_ia()

else:
    boucle_adeux()



printboard(board)






 


