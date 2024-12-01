my_dict = {'Maxim': 2003, 'Oleg': 1996, 'Maria': 1956}
print(my_dict)

print(my_dict['Maxim'])
print(my_dict.get('Denis', 'Такого ключа нет'))

my_dict.update({
    'Sacha': 2001,
    'Kirill': 2005
})

print(my_dict.pop('Maria'))

print(my_dict)


my_set = {1, 2, 3, 1, 2, 3, 4, 5, 6, 7, 6, 5, 4, 3, 'STR', True, (1, 2, 3)}
print(my_set)
my_set.add(12)
my_set.add(16)
my_set.remove(5)

print(my_set)