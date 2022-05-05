import csv
from adapt_csv import Dono_da_bola, Assassinu_Credi, delete_files
from read_csv import final_score


def reader(filename): #Read the log file Function
    game = 0
    kill_list = []
    with open(filename) as f:
        for line in f:
            if ('0:00 InitGame:' in line): #Search for the beggining of the game wich is 0:00 InitGame
                game += 1
                print (game)  
                kill_list.clear()               

            elif ('Kill' in line): #Get all the kill lines and adds then to a csv file
                kill_list.append(line)
                with open(f'game_{game}.csv', 'w+') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(kill_list)


if __name__ == '__main__':
    reader('qgames.log')
    Dono_da_bola()
    Assassinu_Credi()
    delete_files()
    final_score()
    