import random
import string
#import random as rnd

print(string.punctuation)

value = random.randint(100, 200)
my_list = [1,2,3,10,20,30]
choice_from_list = random.choice(my_list)
print(value, choice_from_list)
new_list = my_list.copy()
random.shuffle(new_list)  # shuffle меняет объект! поэтому нужен copy
print(my_list, new_list)

from random import randint
# my_str = 'qwerty'
# choice_from_list = choice(my_str)
# value= randint(100,200)
# print(value)