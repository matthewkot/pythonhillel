my_str = "0123456789"
len_my_str = len(my_str)
print(len_my_str)

number = 12345632234567890
print(len(str(number)))

index = -2
my_str[index] = "E"
print(my_str[index])
print(my_str[len(my_str) -2 ]) # Так лучше не делать!
#Срез

new_str = my_str[:] #от(включая) до ( не включая)
new_str = my_str[1:6:2] # от:до:шаг
p_str = my_str[::2] # четные места в строке
np_str = my_str[1::2] # нечетные места в строке
back_str = my_str [::-1] # разворот строки
print(back_str)

#формат

name = "John"
age = 23

hello_message = f"Знакомтесь, это {name}. Ему {age} года"

print(hello_message)

email= f"{name}.{age}@gmail.com"
print(email)