dict_1 = {1: 1, 2:2}
dict_2 = {11:11, 2:22}

dict_1_keys_set = set(dict_1.keys())
dict_2_key_set = set(dict_2.keys())



# dict_1_keys_set = set(dict_1.keys())
# dict_2_key_set = set(dict_2.keys())
# single_keys = dict_1_keys_set.symmetric_difference(dict_2_key_set)




result_dict = dict_1.copy()
for key in dict_2:
    if key not in result_dict:
        result_dict[key] = dict_2[key]
    else:
        result_dict[key]= [dict_1[key],dict_2[key]]
# print(result_dict)

################################################################################
# dz 9.8
import random
from string import ascii_lowercase as alphabet

def create_email(domains,names):
    domain = random.choice(domains)
    name = random.choice(names)
    number = random.randint(100,999)
    len_str = random.randint(5,7)
    rand_str = "".join([random.choice(alphabet) for _ in range(len_str)])
    return f"{name}.{number}@{rand_str}.{domain}"


names = ["king", "miller", "kean"]
domains = ["net", "com", "ua"]
e_mail = create_email(domains, names)
# print(e_mail)


##################################################################################################
# dz10

def read_txt(filename):
    with open(filename, 'r') as txt_file:
        data = txt_file.readlines()
        data = [line.strip() for line in data]
    return data

def modify_date(date_line):

    parts = date_line.split()
    if len(parts) == 3:
        day = parts[0].rsplit("ndrsth")
        month = parts[0] ## dict_month
        year = parts[2]
        new_date = f"{day}/{month}/{year}"
    return new_date


def get_dates(filename):
    new_dates = []
    data = read_txt(filename)
    for line in data:
        if " - " in line:
            date_line = line.split(" - ")[0]
            new_date = modify_date(date_line)
            if new_date:
                new_dates.append(new_date)
    return new_dates

filename = "../homework/authors.txt"
res = get_dates(filename)
print(res)