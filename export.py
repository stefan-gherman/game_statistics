
# Export functions

from printing import *


options_dict = {'1': print_count_games, '2':print_decide, '3':print_get_latest ,'4':print_count_by_genre, '5':print_get_line_number_by_title, 
'6':print_sort_abc, '7':print_get_genres, '8':print_when_was_top_sold_fps, '9':print_get_most_played, '10':print_sum_sold, 
'11':print_get_selling_avg, '12':print_count_longest_title, '13':print_get_date_avg, '14':print_get_game, 
'15':print_count_grouped_by_genre, '16':print_get_date_ordered}


print('===Menu===')
print('1.Count games')
print('2.Check if a game from year exists in file')
print('3.Get Latest game')
print('4.Count by genre')
print('5.Get line index by title')
print('6.Sort alphabeticaly')
print('7.Get genres')
print('8.When was top fps sold')
print('9.Get most played')
print('10.Total copies sold')
print('11.Sales average')
print('12.Lenght of the longest title')
print('13.Average of dates')
print('14.Get details')
print('15.Group by genre')
print('16.Order by date')

user_choice = input('Choose one of the numbers, anything different will result in the program exiting:')

while user_choice in options_dict.keys():

    print('\n' *3)
    options_dict[user_choice]()
    print('\n' *3)

    print('===Menu===')
    print('1.Count games')
    print('2.Check if a game from year exists in file')
    print('3.Get Latest game')
    print('4.Count by genre')
    print('5.Get line index by title')
    print('6.Sort alphabeticaly')
    print('7.Get genres')
    print('8.When was top fps sold')
    print('9.Get most played')
    print('10.Total copies sold')
    print('11.Sales average')
    print('12.Lenght of the longest title')
    print('13.Average of dates')
    print('14.Get details')
    print('15.Group by genre')
    print('16.Order by date')

    user_choice = input('Choose one of the numbers, anything different will result in the program exiting:')


quit()    