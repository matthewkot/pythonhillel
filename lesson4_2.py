# count = 10
# while count > 0:
#     # count += 1 # увеличение на 1
#     count -=1 # уменьшение на 1
#     print(f"count={count}")
# print("The End")


tmp_value = 5

go_game = True

while go_game:
    value = input("Введи число от 1 до 10")
    if str(tmp_value) == value:
        go_game = False
        print("Cong")


## ДЗ* Давать подсказки пользователям типа: "Попробуй больше"


# while True:
#     value = input("Введи число от 1 до 10")
#     if str(tmp_value) == value:
#         print("Cong")
#         break

