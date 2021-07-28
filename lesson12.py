# функция сортировки

# my_list = [12, 3, 45, 23, -10, 1]
#
# sorted_list = sorted(my_list)
# print(sorted_list)
#
# my_str_list = ["John", "Jack", "Jacob", "Max", "Violeta"]
#
# sorted_str_list = sorted(my_str_list) # по алфавиту
# print(sorted_str_list)
#
# sorted_str_list = sorted(my_str_list, key=len) # по длине
# print(sorted_str_list)


price_list = [{"product": "milk", "price" : 23},
              {"product": "ice-cream", "price": 18},
              {"product": "meat", "price": 120},
              {"product": "Coca-Cola", "price": 10}]

sorted_price_list = sorted(price_list)
print(sorted_price_list)