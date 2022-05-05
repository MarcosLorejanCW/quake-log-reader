import pandas as pd
import numpy as np

def final_score():

    game = 1
    tries = "Lemme see if this works"

    for i in tries:
        try:
            df = pd.read_csv(f'game_{game}_final.csv', sep='" ', engine='python', header=None)
            df.columns = ['0', '1'] 
            del df['0']
            df[['1','2','3','4','5','Player','killed','Death','by','Cause']] = df['1'].str.split(expand=True)
            del df ['1'],df ['2'],df ['3'],df ['4'],df ['5']

            player_kills = df[(df.Player != '<world>')].value_counts('Player')
            player_world_deaths = df[(df.Player == '<world>')].value_counts('Death')

            print(f'game_{game}:')
            print(f'Total Kills: {len(df. index)}')
            print("Players: " , end="")
            print(df['Death'].unique())
            print('Kills:')
            print(player_kills - player_world_deaths)
            print('Death Causes: ')
            print(df['Cause'].value_counts())
            game += 1
        
        except OSError:
            pass




final_score()