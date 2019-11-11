
# Printing functions
from reports import *

filename = 'game_stat.txt'


def print_count_games():
    print(count_games(filename))


def print_decide():
    year = input("Year:")
    print(decide(filename, year))


def print_get_latest():
    print(get_latest(filename))


def print_count_by_genre():
    genre = input("Genre:")
    print(count_by_genre(filename, genre))


def print_get_line_number_by_title():

    title = input("Line:")
    get_line_number_by_title(filename, title)


def print_sort_abc():

    sorted = sort_abc(filename)

    for line in sorted:
        print(line)


def print_get_genres():

    genres = get_genres(filename)

    for line in genres:
        print(line)


def print_when_was_top_sold_fps():
    print(when_was_top_sold_fps(filename))


def print_get_most_played():
    print(get_most_played(filename))


def print_sum_sold():
    print(sum_sold(filename))


def print_get_selling_avg():
    print(get_selling_avg(filename))


def print_count_longest_title():
    print(count_longest_title(filename))


def print_get_date_avg():
    print(get_selling_avg(filename))


def print_get_game():

    title = input("Title:")

    print(get_game(filename, title))


def print_count_grouped_by_genre():

    print(count_grouped_by_genre(filename))


def print_get_date_ordered():

    lst = get_date_ordered(filename)
    for line in lst:
        print(line)
