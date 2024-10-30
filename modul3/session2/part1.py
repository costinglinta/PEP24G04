# dict

my_dict1 = {'example': True}
my_dict2 = dict(test=123)

# update
print(my_dict1)
my_dict1.update({'example2': False})
print(my_dict1)
my_dict1.update(example=None)
print(my_dict1)
my_dict1['example2'] = (False, False)
print(my_dict1)

# get

print(my_dict1.get('example2'))
print(my_dict1)
print(my_dict1.get('example3', "No Value found"))

print(my_dict1['example2'])
# print(my_dict1['example3']) # KeyError: 'example3'

# pop

print(my_dict1)
print(my_dict1.pop('example2'))
print(my_dict1)

# del

del my_dict1['example']
print(my_dict1)

# iter

my_dict2.update({1: 1, 2: 2, 3: 3})
print(my_dict2)

for element in my_dict2:
    print('Element is key: ', element)

for element in my_dict2.keys():
    print('Element is key: ', element)

for element in my_dict2.values():
    print('Element is value: ', element)

for element in my_dict2.items():
    print('Element is item: ', element)

for key, value in my_dict2.items():
    print('Element key is: ', key, 'Element value is: ', value)

