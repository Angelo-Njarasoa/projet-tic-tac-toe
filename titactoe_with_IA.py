import json
import os 
def ia():
    t=1
    
    while t<=9:
    
        if os.path.exists("tictac.json") and os.path.getsize("tictac.json") > 0:
            try:
                with open("tictac.json", "r", encoding="utf-8") as f:
                    data = json.load(f)
            # Si le fichier contient une liste → ancien format → recréation
                if not isinstance(data, dict) or "board" not in data or "dataposition" not in data:
                    raise ValueError("Ancien format détecté")

                board = data["board"]
                dataposition = data["dataposition"]
            except json.JSONDecodeError:
        # fichier corrompu → on repart d’une grille vide
                board = [
                    ["*", " ", "*", " ", "*"],
                    ["*", " ", "*", " ", "*"],
                    ["*", " ", "*", " ", "*"]
                ]   
                dataposition=[]
        else:
            board = [
                ["*", " ", "*", " ", "*"],
                ["*", " ", "*", " ", "*"],
                ["*", " ", "*", " ", "*"]               
            ]
            dataposition=[]
                         
        if t%2==0 and t<=9:
            signe="X"
            print("tour des X")
            p = int(input("nouveau coup: "))
        elif t%2>0 and t<=9:
            print("tour des O")
            signe="O"
            winning_sets = [
                {7, 8, 9}, {4, 5, 6}, {1, 2, 3},
                {7, 4, 1}, {8, 5, 2}, {9, 6, 3},
                {7, 5, 3}, {1, 5, 9}
            ]

            for winning_set in winning_sets:
                existing = winning_set & set(dataposition)
                missing = winning_set - existing
                if missing:
                    p = missing.pop()

            

        
        if p not in dataposition: 
            dataposition.append(p)
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
            json.dump({"board":board,"dataposition":dataposition},f,ensure_ascii=False)
        
        if t == 9 or p==0:
            board = [
                ["*", " ", "*", " ", "*"],
                ["*", " ", "*", " ", "*"],
                ["*", " ", "*", " ", "*"]
            ]
            dataposition=[]
            t=0
            print ("nouvelle partie !")
        t+=1
        with open("tictac.json",'w',encoding='utf-8') as f:
            json.dump({"board":board,"dataposition":dataposition},f,ensure_ascii=False)
ia()