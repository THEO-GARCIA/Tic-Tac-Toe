import random

#plateaux de jeu
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-",]

player="O"

gagnant=None

game=True

#creation du plateaux

def printboard(board):
    print(board[0] + " | " + board[1] + " | " + board[2])
    print("---------")
    print(board[3] + " | " + board[4] + " | " + board[5])
    print("---------")
    print(board[6] + " | " + board[7] + " | " + board[8])

#entre la valeur desire

def playerinput(board):
    chiffre=int(input("Entre un chiffre en 1 et 9: "))
    if chiffre >=1 and chiffre <=9 and board[chiffre -1]== "-":
        board[chiffre -1] = player
    else:
        print("C'est place est deja prise.")



#verif si win ou pas

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
    if win_diag(board) or win_horizontal(board) or win_vertical(board):
        print(f"Le gagnant es {gagnant} !")
    
def verif_nul(board):
    global game
    if "-" not in board:
     printboard(board)
     print("Match nul !!!!")
     game=False

def changement():
    global player
    if player == "X":
        player= "O"
    else:
        player="X"

#ia

def ia(board):
    while player == "X":
        position= random.randint (0,8)
        if board[position]=="-":
            board[position]="X"
            changement()




while game:
    printboard(board)
    playerinput(board)
    verif_nul(board)
    changement()
    ia(board)
    verif_gagnant()
    verif_nul(board)







