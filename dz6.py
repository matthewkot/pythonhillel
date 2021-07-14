my_list = ["chen", "slardar", "beastmaster", "puck", "weaver"]
new_list = []
for index, symbol in enumerate(my_list):
    if index % 2:
        new_list.append(symbol[::-1])
    else:
        new_list.append(symbol)
# print(new_list)
#####################################################################


my_list = ["as", "da", "an", "love","defense", "of the", "ancients"]
first_a_list = []
for index, symbol in enumerate(my_list):
    if symbol[0] == 'a':
        first_a_list.append(symbol)
# print(first_a_list)
#####################################################################


my_list = ["as", "da", "an", "love","defense", "of the", "ancients"]
a_list = []
for index, value in enumerate(my_list):
    if 'a' in value:
        a_list.append(value)

# a_list = [a_list for a_list in my_list if "a" in a_list]
# print(a_list)
#####################################################################


my_list = [1, 2, 3, "11", "22", 33]
str_list = []
for index, symbol in enumerate(my_list):
    if isinstance(symbol, str):
        str_list.append(symbol)
# print(str_list)
#####################################################################


my_str = "simpledimplepopitsqiush"
my_list = []
for index, symbol in enumerate(set(my_str)):
    if my_str.count(symbol) == 1:
        my_list.append(symbol)
# print(my_list)
#####################################################################

my_str = "simpledimplepopitsqiush"
my_second_str = "qwertyuiopasdfghjkkzxcn"
my_list = []
my_list.append((set(my_str).intersection(set(my_second_str))))
# print(my_list)
#####################################################################

my_str = "simpledimplepopitsqiush"
my_second_str = "qwertyuiopasdfghjkkzxcn"
res = []
# for index_1, symbol_1 in enumerate(my_str):
#     if my_str.count(symbol_1) == 1:
#         my_list_1.append(symbol_1)
# for index_2, symbol_2 in enumerate(my_second_str):
#     if my_second_str.count(symbol_2) == 1:
#         my_list_2.append(symbol_2)
# my_list.append(set(my_list_1).intersection(set(my_list_2)))

my_list = list(set(my_str).intersection(set(my_second_str)))
for index, symbol in enumerate(my_list):
    if my_str.count(symbol) == 1 and my_second_str.count(symbol) == 1:
        res.append(symbol)
print(res)
#####################################################################


Artur = {'Фамилия': 'Шах',
        'Имя': 'Артур',
        'Возраст': 22,
        'Проживание': {
            'Страна': 'Украина',
            'Город': 'Днепр',
            'Улица': 'ул.Богдановская'
        },
        'Работа': {
            'Наличие': True,
            'Должность': 'Junior QA'
        }}
# print(Artur)
#####################################################################


weight = 'г'
maybe_cake = {'Составляющие': {'Коржи': {'Мука': f'300{weight}',
                                        'Молоко': f'400{weight}',
                                        'Масло': f'100{weight}',
                                        'Яйцо': f'130{weight}'
                                        },
                              'Крем': {'Сахар': f'150{weight}',
                                       'Масло': f'70{weight}',
                                       'Ваниль': f'30{weight}',
                                       'Сметана': f'400{weight}'
                                       },
                              'Глазурь': {'Какао': f'180{weight}',
                                          'Сахар': f'50{weight}',
                                          'Масло': f'40{weight}'
                                          }
                              }
             }
# print(maybe_cake)

