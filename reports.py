
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


def get_latest(lst):
    GAME_YEAR = 2
    GAME_TITLE = 0

    late_year = -1

    for sublist in range(len(lst)):
        if int(lst[sublist][GAME_YEAR]) > late_year:
            late_year = int(lst[sublist][GAME_YEAR])
            title = lst[sublist][GAME_TITLE]
    return title

text_file = open_file()


