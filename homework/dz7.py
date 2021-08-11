from collections import defaultdict

persons = [{"name": "John", "age": 15}, {"name": "Johny", "age": 16},
           {"name": "Matthew", "age": 17}, {"name": "Artur", "age": 18},
           {"name": "Dmitriy", "age": 19}, {"name": "Jack", "age": 15}]

age_by_names = defaultdict(list)
len_name_by_names = defaultdict(list)
ages = []

for person in persons:
    name = person["name"]
    age = person["age"]
    age_by_names[age].append(name)
    len_name_by_names[len(name)].append(name)
    ages.append(age)

min_age = min(age_by_names)
print('min_age:', *age_by_names[min_age])

max_len_name = max(len_name_by_names)
print('max_len_name:', *len_name_by_names[max_len_name])

print('average:', sum(ages) // len(ages))



my_dict_1 = {1: 1, 2: 2, 3: 3, "four": 4 , "five": 3}
my_dict_2 = {11: 12, 13: 14, 15: "four", 1: 3}

my_dict_1_keys = my_dict_1.keys()
my_dict_2_keys = my_dict_2.keys()

my_dict_1_keys_set = set(my_dict_1_keys)
my_dict_2_keys_set = set(my_dict_2_keys)
both_dicts_keys = list(my_dict_1_keys_set.intersection(my_dict_2_keys_set))

unique_first_dict_keys = list(my_dict_1_keys_set.difference(my_dict_2_keys_set))

new_dict = {}
for unique_first_dict_key in unique_first_dict_keys:
    new_dict[unique_first_dict_key] = my_dict_1[unique_first_dict_key]


result_dict = {}
value_list = []

for key, value in my_dict_1.items():
    if key in my_dict_2_keys:
        value_list.append(value)
        value_list.append(my_dict_2[key])
        result_dict[key] = value_list
        value_list = []
    else:
        result_dict[key] = value
for key_2, value_2 in my_dict_2.items():
    if key_2 not in result_dict.keys():
        result_dict[key_2] = value_2