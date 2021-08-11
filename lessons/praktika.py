# my_str = "blablacarblablacar"
# my_symbol = "bla"
#
# my_symbol_count = my_str.count(my_symbol)
# print(my_symbol_count)

# res_message = f"{my_symbol}\n" * my_symbol_count
# print(res_message.strip())
# for _ in range(my_symbol_count):
#     print(my_symbol)
    # print(my_symbol * _ )


# my_str = "bla BLA car"
# my_str = my_str.lower()
# symbols_heap = []
# for symbol in my_str:
#     if symbol not in symbols_heap:
#         symbols_heap.append(symbol)
# res_len = (len(symbols_heap))
# print(res_len)


# my_str = "qwerty"
# my_list = []
# for index in range(len(my_str)):
#     if not index % 2:
#         symbol = my_str[index]
#         my_list.append(symbol)
# print(my_list)

# for index, symbol in enumerate(my_str):
#     if not index % 2:
#         my_list.append(symbol)
# print(my_list)


# my_str = "qwerty"
# my_list = []
# str_index = [3, 2, 5, 5, 1, 0, 5, 0, 3, 2, 1]
#
# for index in str_index:
#     symbol = my_str[index]
#     my_list.append(symbol)
# print(my_list)


# my_number = 1234567890987654345678987654741052963
# digit_count = len(str(my_number))
# print(digit_count)new_number_str = number_str


# number_str = str(my_number)
# max_symbol = max(number_str)
# print(max_symbol)
#
# test_list = ["1", "2", "3", "4"]
# print(max(test_list))


# number_str = str(my_number)
# new_number_str = number_str[::-1]
# new_number = int(new_number_str)
# print(new_number)
#
# new_number = int(str(my_number)[::-1])
# print(new_number)


# my_list = [1,2,5,3,-8,4]
# my_str = 'qwerty'
# sorted_list = sorted(my_list)
# print(sorted_list)
my_number = 123123
number_str = str(my_number)
sorted_number_symbols_list = sorted(number_str)
new_number_str = ''.join(sorted_number_symbols_list)
new_number = int(new_number_str)
print(new_number)