
def reverse_str_function(new_list: list) -> list:
    new_str = []
    for index, symbol in enumerate(new_list):
        if index % 2:
            new_str.append(symbol[::-1])
        else:
            new_str.append(symbol)
    return new_str


my_list = ["chen", "slardar", "beastmaster", "puck", "weaver"]
result =  reverse_str_function(my_list)
print(result)


def first_a_list(new_list: list) -> list:
    first_a_list = []
    for index, symbol in enumerate(new_list):
        if symbol[0] == 'a':
            first_a_list.append(symbol)
    return first_a_list

my_list = ["as", "da", "an", "love", "defense", "of the", "ancients"]
result = first_a_list(my_list)
print(result)



def symbol_a_in_word(new_list : list) -> list:
    a_list = []
    for index, value in enumerate(new_list):
        if 'a' in value:
            a_list.append(value)
    return a_list

my_list = ["as", "da", "an", "love","defense", "of the", "ancients"]
result = symbol_a_in_word(my_list)
print(result)



def str_int_checker(new_list : list) -> list:
    str_list = []
    for index, symbol in enumerate(new_list):
        if isinstance(symbol, str):
            str_list.append(symbol)
    return str_list


my_list = [1, 2, 3, "11", "22", 33]
result= str_int_checker(my_list)
print(result)



def unique_symbol(new_str : str) -> list:
    my_list = []
    for index, symbol in enumerate(set(new_str)):
        if my_str.count(symbol) == 1:
            my_list.append(symbol)
    return my_list

my_str = "simpledimplepopitsqiush"
result = unique_symbol(my_str)
print(result)


def two_string_intersection(new_str_1 : str , new_str_2 : str) -> list:
    my_list = list(set(new_str_1).intersection(set(new_str_2)))
    return my_list

my_str = "simpledimplepopitsqiush"
my_second_str = "qwertyuiopasdfghjkkzxcn"
result = two_string_intersection(my_str,my_second_str)
print(result)

def unique_symbol_two_string(new_str_1 : str, new_str_2 : str) -> list:
    res = []
    my_list = list(set(new_str_1).intersection(set(new_str_2)))
    for index, symbol in enumerate(my_list):
        if new_str_1.count(symbol) == 1 and new_str_2.count(symbol) == 1:
            res.append(symbol)
    return res

my_str = "simpledimplepopitsqiush"
my_second_str = "qwertyuiopasasdasdasdfghjkkzxcn"
result = unique_symbol_two_string(my_str, my_second_str)
print(result)



import random
import string


names = ['Smith', 'Jonson', 'Williams', 'Brown', 'Davis', 'Jones', 'Garcia', 'Miller', 'Davis']
domains = ['com', 'net', 'org', 'in', 'uk', 'co', 'us', 'ua', 'uk', 'au', 'de']


def email_generation_func(names_list : list, domains_list : list ) -> str:
    random_name = random.choice(names_list).lower()
    random_number = random.randint(100,999)
    letters = string.ascii_lowercase
    random_letters = []
    for count in range(random.randint(5, 7)):
        random_letter = random.choice(letters);
        random_letters.append(random_letter)
    random_letter_str = ''.join(random_letters)
    random_domain = random.choice(domains_list)
    email = f'{random_name}.{random_number}@{random_letter_str}.{random_domain}'
    return email


random_email = email_generation_func(names, domains)
print(random_email)