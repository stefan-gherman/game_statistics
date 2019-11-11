
# Report functions
def insertion_sort(lst):
    for i in range(1,len(lst)):
        current = lst[i]
        j = i - 1

        while j >= 0 and current < lst[j]:
            lst[j+1] = lst[j]
            j -= 1
        lst[j+1] = current    
    
    return lst            

def selection_sort(lst):
    for i in range(len(lst)):
        index_min = i

        for j in range(i+1, len(lst)):
            if lst[index_min] > lst[j]:
                index_min = j
        lst[i],lst[index_min] = lst[index_min], lst[i]        
    return lst    

def open_file(filename):

    with open (filename) as game_text:

        games_db = game_text.readlines()

    

    for line in range(len(games_db)):
        games_db[line] = games_db[line].rstrip('\n').split('\t')

    return games_db

def count_games(filename):
    lst = open_file(filename)
    return len(lst)


def decide(filename, year):
    GAME_YEAR = 2
    lst = open_file(filename)
    for sublist in range(len(lst)):
        if lst[sublist][GAME_YEAR] == str(year):
            return True
    return False        


def get_latest(filename):
    GAME_YEAR = 2
    GAME_TITLE = 0
    lst = open_file(filename)
    late_year = -1

    for sublist in range(len(lst)):
        if int(lst[sublist][GAME_YEAR]) > late_year:
            late_year = int(lst[sublist][GAME_YEAR])
            title = lst[sublist][GAME_TITLE]
    return title


def count_by_genre(filename, genre):
    GAME_GENRE = 3
    lst = open_file(filename)
    current_genre_count = 0
    for sublist in range(len(lst)):
        if lst[sublist][GAME_GENRE] == str(genre):
            current_genre_count += 1 
    return current_genre_count        


def get_line_number_by_title(filename, title):
    GAME_TITLE = 0
    lst = open_file(filename)
    for sublist in range(len(lst)):
        if lst[sublist][GAME_TITLE] == str(title):
            return sublist + 1
    raise ValueError('Non-existing game')        

def sort_abc(filename):

    GAME_TITLE = 0

    lst = open_file(filename)

    titles = []

    for sublist in range(len(lst)):
        titles.append(lst[sublist][GAME_TITLE])

    titles = selection_sort(titles)

    return titles    


def get_genres(filename):
    lst = open_file(filename)
    GAME_GENRE = 3

    genres = []

    for sublist in range(len(lst)):
        if lst[sublist][GAME_GENRE] not in genres:
            genres.append(lst[sublist][GAME_GENRE])
    genres = selection_sort(genres)
    return genres        

def when_was_top_sold_fps(filename):

    lst = open_file(filename)

    GAME_YEAR = 2
    GAME_SALES = 1
    GAME_GENRE = 3

    SEARCH_GENRE = 'First-person shooter'

    

    if SEARCH_GENRE not in get_genres(filename):
        raise ValueError


         

    year = -1
    sales = -1
    for sublist in range(len(lst)):
        if lst[sublist][GAME_GENRE] == SEARCH_GENRE:
            if float(lst[sublist][GAME_SALES]) > sales:
                sales = float(lst[sublist][GAME_SALES])
                year = lst[sublist][GAME_YEAR]

    return float(year)            


def get_most_played(filename):
    lst = open_file(filename)

    GAME_TITLE = 0
    GAME_SALES = 1

    max_sales = -1

    for sublist in range(len(lst)):
        if float(lst[sublist][GAME_SALES]) > max_sales:
            max_sales = float(lst[sublist][GAME_SALES])
            name = lst[sublist][GAME_TITLE]
    
    return name

def sum_sold(filename):

    lst = open_file(filename)

    GAME_SALES = 1

    total_sales = 0

    for sublist in range(len(lst)):
        total_sales += float(lst[sublist][GAME_SALES])   

    return total_sales    


def get_selling_avg(filename):

    lst = open_file(filename)

    total_sum = sum_sold(filename)

    return total_sum / len(lst)

def count_longest_title(filename):
    
    lst = open_file(filename)

    GAME_TITLE = 0

    len_name = -1

    for sublist in range(len(lst)):
        if len(lst[sublist][GAME_TITLE]) > len_name:
            len_name = len(lst[sublist][GAME_TITLE])

    return len_name        