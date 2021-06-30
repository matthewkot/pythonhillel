my_int = 1020301234
zero_count = str(my_int).count("0")
print(zero_count)
##################################################


my_int = 1020301234000010
zero_count = 0
while my_int % 10 == 0:
    zero_count += 1
    my_int //= 10
print(zero_count)
##################################################


my_list_1 = [1, 3, 5, 7, 9]
my_list_2 = [2, 4, 6, 8, 0]
my_result = []
for index, symbol in enumerate(my_list_1):
    if not index % 2:
        my_result.append(symbol)
for index, symbol in enumerate(my_list_2):
    if index % 2:
        my_result.append(symbol)
print(my_result)
##################################################


my_list = [1, 2, 3, 4]
firs_num = my_list.pop(0)
new_list = my_list.copy()
new_list.append(firs_num)
print(new_list)
##################################################


my_list = [5, 6, 7, 8]
firs_num = my_list.pop(0)
my_list.append(firs_num)
print(my_list)
##################################################


my_str = "88 больше чем 77 но меньше чем 99"
my_list = my_str.split()
numbers = []
for index in my_list:
    if index.isdigit():
        numbers.append(int(index))
numbers_sum = sum(numbers)
print(numbers_sum)
##################################################


my_str = 'Might and Heroes'
l_limit = 'i'
r_limit = 'h'
l_limit_index = my_str.lower().find(l_limit)
r_limit_index = my_str.lower().rfind(r_limit)
sub_str = my_str[l_limit_index + 1: r_limit_index]
print(sub_str)
##################################################


my_str = "qwerty123"
my_list = []
for index in range(0, len(my_str), 2):
    sub_str = my_str[index:index+2]
    if len(sub_str) == 2:
        my_list.append(sub_str)
    else:
        sub_str = sub_str+'_'
        my_list.append(sub_str)
print(my_list)
##################################################


my_list = [2,4,1,5,3,9,0,7]
counter = 0
for i in range(1, len(my_list) - 1):
    if my_list[i - 1] < my_list[i] and my_list[i] > my_list[i + 1]:
        counter += 1
print(counter)