
# Report functions

def open_file():

    with open ('game_stat.txt') as game_text:

        games_db = game_text.readlines()

    

    for line in range(len(games_db)):
        games_db[line] = games_db[line].rstrip('\n').split('\t')

    return games_db

def count_games(lst):
    return len(lst)


def decide(lst, year):
    GAME_YEAR = 2

    for sublist in range(len(lst)):
        if lst[sublist][GAME_YEAR] == str(year):
            return True
    return False        

text_file = open_file()


