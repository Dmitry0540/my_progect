immutable_va= 10, 12, 16, 20, 'apple', 'green'
print(immutable_va) # Главное свойство кортежа - это невозможность изменить содержимое кортежа
# после его создания
# Можно изменить только в том случае , если перевести в список
immutable_va2= ['tap', 'love'], 100, 200
immutable_va2[0][1]= "stop"
print(immutable_va2)


mutable_list= [10, 12, 16, 20, 'apple', 'green']
print(mutable_list)
mutable_list[2]= 'milk'
print(mutable_list)
mutable_list.append('Ghost')
print(mutable_list)
