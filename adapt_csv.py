import os

def Dono_da_bola (): #Changed the the Dono da Bola to Dono_da_Bola
    game = 2
    tries = "At least i'm trying"
    try:
        for a in tries:
            text = open(f"game_{game}.csv", "r")
            text = ''.join([i for i in text]).replace("Dono da Bola", "Dono_da_Bola")
            x = open(f"game_{game}_new.csv","w")
            x.writelines(text)
            x.close()
            game += 1
            

    except OSError:
        print ("All Dono da Bola was changed to Dono_da_Bola")
        return

def Assassinu_Credi(): #Changed the the Assasinu Credi to Assasinu_Cred
    game = 2
    tries = "At least i'm trying"
    try:
        for i in tries:
            text = open(f"game_{game}_new.csv", "r")
            text = ''.join([i for i in text]).replace("Assasinu Credi", "Assasinu_Credi")
            x = open(f"game_{game}_final.csv","w")
            x.writelines(text)
            x.close()
            game += 1
            
    except OSError:
        print ("All Assasinu Credi was changed to Assasinu_Credi")
        return

def delete_files(): #Delete the extra files created and add _final do game_1 name
    game = 2
    tries = "At least i'm trying"
    try:
        for i in tries:
            os.remove(f'game_{game}.csv')
            os.remove(f'game_{game}_new.csv')
            game += 1

    except OSError:
        old_name = "game_1.csv"
        new_name = "game_1_final.csv"
        
        if os.path.isfile(new_name):
            pass
        else:
            os.rename(old_name, new_name)
            print("All unwanted files were deleted.")
            pass



