import json
import os 
import random
def ia():
    t=1
    
    while t<=9:
        print(int(t))
        if os.path.exists("tikctac.json") and os.path.getsize("tikctac.json") > 0:
            try:
                with open("tikctac.json", "r", encoding="utf-8") as f:
                    data = json.load(f)
            # Si le fichier contient une liste → ancien format → recréation
                if not isinstance(data, dict) or "board" not in data or "position_joueur" not in data or "position_ia" not in data:
                    raise ValueError("Ancien format détecté")

                board = data["board"]
                position_joueur = data["position_joueur"]
                position_ia= data["position_ia"]
            except json.JSONDecodeError:
        # fichier corrompu → on repart d’une grille vide
                board = [
                    ["*", " ", "*", " ", "*"],
                    ["*", " ", "*", " ", "*"],
                    ["*", " ", "*", " ", "*"]
                ]   
                position_joueur=[]
                position_ia=[]
        else:
            board = [
                ["*", " ", "*", " ", "*"],
                ["*", " ", "*", " ", "*"],
                ["*", " ", "*", " ", "*"]               
            ]
            position_joueur=[]
            position_ia=[]
                         
        
        if t%2>0 and t<=9:
            print("tour des O")
            signe="O"
            winning_sets = [
                {7, 8, 9}, {4, 5, 6}, {1, 2, 3},
                {7, 4, 1}, {8, 5, 2}, {9, 6, 3},
                {7, 5, 3}, {1, 5, 9}
            ]

            for winning_set in winning_sets:
                existing = winning_set & set(position_ia)
                missing = winning_set - existing
                existing2 = winning_set & set(position_joueur)
                missing2 = winning_set - existing2

                if len(missing)==1:
                    coup = next(iter(missing))
                    if coup not in position_joueur:
                        p = coup
                        break
                elif len(missing2)==1:
                    coup2 = next(iter(missing2))
                    if coup2 not in position_ia:
                        p = coup2
                        break

            else:
                clavier = {1,2,3,4,5,6,7,8,9}
                randomcoup = clavier - set(position_ia) - set(position_joueur)
                p = random.choice(list(randomcoup))

        if t%2==0 and t<=9:
            signe="X"
            print("tour des X")
            p = int(input("nouveau coup: "))
        elif t==1 :
            print("tour des O")
            signe="O"
            p= random.randint(1, 9)

            

        
        if p not in position_joueur and t%2==0 : 
            position_joueur.append(p)
        if p not in position_ia and t%2>0 : 
            position_ia.append(p)
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
        with open("tikctac.json",'w',encoding='utf-8') as f:
            json.dump({"board":board,"position_joueur":position_joueur,"position_ia":position_ia},f,ensure_ascii=False)
        
        if t == 9 or p==0:
            board = [
                ["*", " ", "*", " ", "*"],
                ["*", " ", "*", " ", "*"],
                ["*", " ", "*", " ", "*"]
            ]
            position_joueur=[]
            position_ia=[]
            t=0
            print ("nouvelle partie !")
        t+=1
        with open("tikctac.json",'w',encoding='utf-8') as f:
            json.dump({"board":board,"position_joueur":position_joueur,"position_ia":position_ia},f,ensure_ascii=False)
ia()