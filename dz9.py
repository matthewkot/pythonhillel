import os
import re

def get_domains(file_name: str) -> list:
    with open(file_name, 'r') as txt_file:
        data = txt_file.read()
        data = data.replace('.', '')
        domains_list = data.split('\n')
    return domains_list


domains = get_domains('txt_folder/domain.txt')
print(f'Domains list: {domains}')

####################################################

def get_last_names(file_name: str) -> list:
    last_names_list = []
    file_lines_list = get_file_lines(file_name)
    for line in file_lines_list:
        line = line.split('\t')
        last_names_list.append(line[1])
    return last_names_list


def get_file_lines(file_name: str):
    with open(file_name, 'r') as txt_file:
        data = txt_file.read()
        lines_list = data.split('\n')
    return lines_list


last_names = get_last_names('txt_folder/names.txt')
print(f'Last names list: {last_names}')




############################################################
def read_txt(filename: str ) -> dict:
    with open(filename, 'r') as txt_file:
        data = txt_file.readlines()
        data = [line.strip() for line in data]
    return data

def modify_date(date_line: str ) -> dict:
    new_date = ""
    parts = date_line.split()
    if len(parts) == 3:
        day = parts[0].rstrip("ndrsth")
        if len(day) == 1:
            day = f"0{day}"
        # day = day if len(day) == 2 else f"0{day}"
        monts = parts[1]  ## dict_monts
        year = parts[2]
        new_date = f"{day}/{monts}/{year}"
    return new_date


def get_dates(filename : str ) -> dict:
    new_dates = []
    data = read_txt(filename)
    for line in data:
        if " - " in line:
            date_line = line.split(" - ")[0]
            new_date = modify_date(date_line)
            if new_date:
                new_dates.append(new_date)
    return new_dates


filename = "txt_folder/authors.txt"
res = get_dates(filename)
print(res)




