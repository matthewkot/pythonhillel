value = input("Введи целое число")
# if value.isdigit():
#     value = float(value)
#     result = value * 2
#     print(result)
# else:
#     print("Вы ввели не число")


try:
    value = float(value)
    result = 1 / value
except (ValueError, ZeroDivisionError) :
    print("Попробуй ещё")
    result = 3
except ValueError :
    print("Вы дура4ек")
    result = 0
except ZeroDivisionError :
    print("Вы полный дура4ек")
    result = -1


print(result)

