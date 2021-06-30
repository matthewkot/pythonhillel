my_list = [1, 10, 100, 1000, 100000]
for element in my_list:
    if element > 100:
        print(element)
#####################################

my_list = [1, 10, 100, 1000, 100000]
my_result = []
for element in my_list:
    if element > 100:
        my_result.append(element)
print(my_result)
#####################################


my_list = [1, 2, 3, 4, 5]
for element in my_list:
    if len(my_list) < 2:
        my_list.append(0)
    elif len(my_list) >= 2:
        my_list.append(my_list[-1]+my_list[-2])
    print(my_list)
    break
###############################################


try:
    value = float(input("Print numb"))
    print(value ** -1)
except ValueError:
    print("Print num!")
except ZeroDivisionError:
    print("0 is not a number")
#######################################


my_string= "0123456789"
my_list = []
for symb_1 in my_string:
	for symb_2 in my_string:
            my_list.append(int(symb_1 + symb_2))
print(my_list)
