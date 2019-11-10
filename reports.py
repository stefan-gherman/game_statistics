
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


def count_by_genre(lst, genre):
    GAME_GENRE = 3

    current_genre_count = 0
    for sublist in range(len(lst)):
        if lst[sublist][GAME_GENRE] == str(genre):
            current_genre_count += 1 
    return current_genre_count        


def get_line_number_by_title(lst, title):
    GAME_TITLE = 0

    for sublist in range(len(lst)):
        if lst[sublist][GAME_TITLE] == str(title):
            return sublist + 1
    raise ValueError('Non-existing game')        







