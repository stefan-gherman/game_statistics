
# Report functions

def open_file():

    with open ('game_stat.txt') as game_text:

        games_db = game_text.readlines()

    

    for line in range(len(games_db)):
        games_db[line] = games_db[line].rstrip('\n').split('\t')

    return games_db

def count_games(lst):
    return len(lst)

text_file = open_file()
print(count_games(text_file))

