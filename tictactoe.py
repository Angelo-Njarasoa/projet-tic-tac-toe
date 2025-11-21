import json
import os
def ia():
    t=1
    
    while t<=9:
    
        if os.path.exists("tictac.json") and os.path.getsize("tictac.json") > 0:
            try:
                with open("tictac.json", "r", encoding="utf-8") as f:
                    board = json.load(f)
            except json.JSONDecodeError:
        # fichier corrompu → on repart d’une grille vide
                board = [
                    [" ", " ", " ", " ", " "],
                    [" ", " ", " ", " ", " "],
                    [" ", " ", " ", " ", " "]
                ]
        else:
            board = [
                [" ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " "]
            ]

        if t%2==0 and t<=9:
            signe="X"
        elif t%2>0 and t<=9:
            signe="O"
        p= int(input())
        if p==7:
            board[0][0]=signe
        elif p==8:
            board[0][2]=signe
        elif p==9:
            board[0][4]=signe 
        elif p==4:
            board[1][0]=signe 
        elif p == 5:
            board[1][2] = signe
        elif p == 6:
            board[1][4] = signe
        elif p == 1:
            board[2][0] = signe
        elif p == 2:
            board[2][2] = signe
        elif p == 3:
            board[2][4] = signe
        
        
        for row in board:
            print(" ".join(row))
        with open("tictac.json",'w',encoding='utf-8') as f:
            json.dump(board,f,ensure_ascii=False)
        if t == 9 or p==0:
            board = [
                [" ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " "],
                [" ", " ", " ", " ", " "]
            ]
            t=0
            print ("nouvelle partie !")
        t+=1
        with open("tictac.json",'w',encoding='utf-8') as f:
            json.dump(board,f,ensure_ascii=False)
ia()
        