first= int(input('Введите первое значение: '))
second=int(input('Введите второе значение: '))
therd=int(input('Введите третье значение: '))

if first==second==therd:
    print('Значение: 3')
elif first== second and first==therd or second == therd:
    print('Значение: 2')
else:
    print('Значение: 0')