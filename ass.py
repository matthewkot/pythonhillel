import os
import re

month = {'January': '01',
         'February': '02',
         'March': '03',
         'April': '04',
         'May': '05',
         'June': '06',
         'July': '07',
         'August': '08',
         'September': '09',
         'October': '10',
         'November': '11',
         'December': '12'}


def get_original_dates(file_name: str) -> list:
    dates_original_list = []
    file_lines_list = get_file_lines(file_name)
    for line in file_lines_list:
        line = line.split(' - ')
        for item in line:
            if re.search(r"[0-31][a-z]{2}\s.+", item):
                dates_original_list.append(item)
    return dates_original_list


def get_date_modified(file_name: str):
    dates_original_list = get_original_dates(file_name)
    dates_modified_list = []
    for date in dates_original_list:
        date = date.split(' ')
        day_of_the_month = date[0]
        day_of_the_month = day_of_the_month.rstrip('ndrsth')
        if int(day_of_the_month) < 10:
            modified_day_of_the_month = f'0{day_of_the_month}'
        else:
            modified_day_of_the_month = day_of_the_month
        modified_month = month[date[1]]
        if len(date) == 3:
            year = date[2]
            modified_date = f'{modified_day_of_the_month}/{modified_month}/{year}'
        else:
            modified_date = f'{modified_day_of_the_month}/{modified_month}'
        dates_modified_list.append(modified_date)
    return dates_original_list, dates_modified_list


def create_final_dicts_list(file_name: str) -> list:
    final_dicts_list = []
    date_lists_tuple = get_date_modified(file_name)
    dates_original_list = date_lists_tuple[0]
    dates_modified_list = date_lists_tuple[1]
    for index, date in enumerate(dates_original_list):
        dates_dict = {'date_original': date, 'date_modified': dates_modified_list[index]}
        final_dicts_list.append(dates_dict)
    return final_dicts_list


result_dates_list = create_final_dicts_list('txt_folder/authors.txt')
print(f'Dates list: {result_dates_list}')