# # if
#
# value =42 #Условие
#
# if value ==4: #Блок если да
#     print("Artur loh")
#     print(value * 3)
#     new_value = "asd" * value
#     print(new_value)
#
# else: #Блок если нет
#     print("Else case")
#
# print("The End")

value = "abc"
new_value = bool(value)

value = 10 #Всегда true,кроме 0

if value:
    print(value)

print("The end")

value = 0.0 #

if value:
    print(value)

print("The end")

my_bool = False

value = str(my_bool)

if value:
    print(value)
print("The End")

value = 15
if not value % 2 and not value % 3:
    print("Число делится и на 2 и на 3 - т.е на 6")
elif not value % 2:
    print("Число делится только на 2")
elif not value % 3:
    print("Число делится только на 3")
else:
    pass

my_str = "qwerty"
my_int = 10

if "r" in my_str:
    new_str = my_str * 2
else:
    new_str = my_str

new_str = my_str * 2 if "r" in my_str else my_str #Тернарный оператор
new_int = my_int // 2 if my_int > 10 else -1
print(new_int)
print(new_str)

