value = 15
new_value = value / 2 if value < 100 else - value
print(new_value)
###############################
value = 500
new_value = 1 if value < 100 else 0
print(new_value)
################################
value = 10
new_value = True if value < 100 else False
print(new_value)
################################


my_str = "slOvo"
my_str.upper()
################################


my_str = "slOvo"
my_str.lower()
################################


my_str = "qwer"
if len(my_str) < 5:
    new_str = my_str * 2
else:
    new_str = my_str
print(new_str)
################################


my_str = "qwer"
if len(my_str) < 5:
    back_str = my_str + my_str[::-1]
else:
    back_str = my_str
print(back_str)
################################
