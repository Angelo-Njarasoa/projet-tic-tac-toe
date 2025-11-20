import json
import os
def ia():
    t=1
    while t<=10:
        if t%2==0:
            signe="x"
        else:
            signe="o"
        p= input()
        if p==7:
            board[0[0]]=signe
        elif p==8:
            board[0[1]]=signe
        elif p==9:
            board[0][2]=signe 
        elif p==4:
            board[1][0]=signe 
        elif p == 5:
            board[1][1] = signe
        elif p == 6:
            board[1][2] = signe
        elif p == 1:
            board[2][0] = signe
        elif p == 2:
            board[2][1] = signe
        elif p == 3:
            board[2][2] = signe
        t+=1      
    fichier = "tictactoe.json"

# Charger les anciennes données si le fichier existe et n'est pas vide
    if os.path.exists(fichier) and os.path.getsize(fichier) > 0:
        with open(fichier, "r") as f:
            board = json.load(f)
    else:
        board = [[][][]]  # sinon créer une liste vide

# Exemple : nouvelle donnée venant de ton script
    nouveau_mot = signe  # <-- ici tu mets ton data actuel
    if nouveau_mot:  # seulement si ce n'est pas vide
        board.append(nouveau_mot)

# Réécrire le fichier JSON avec les nouvelles données
    with open(fichier, "w") as f:
        json.dump(data, f, separators=(",", ":"))

print("Données mises à jour :", data)
        print("bingo !")
        for y in board:
            print (y)
    else:
        print("pas de morpion")
ia() 