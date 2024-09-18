my_dict={'Dany': 856243443, 'Anton': 85423574866435, 'Igor': 2022}
print('Словарь: ',my_dict)
print('Номер телефона:', my_dict.get('Dany'))
print(my_dict.get('Anna', 'Нет таких данных'))
print('Удаление элемента "Антон":',my_dict.pop('Anton'))

my_dict.update({'Sister': 2002, 'brat': 1969})
print(my_dict.items())

print()
print()




my_set= {1,2,6,5,4,2,3,4,5,8,9,7}
print('Множество:',set(my_set))
my_set.update({10, 0})
my_set.add('test')
my_set.add('list')
print('Измененное множество:', my_set)
my_set.discard(3)
print('Финальная версия',my_set)