my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
log = 0
while len(my_list) > log:
    if my_list[log] < 0:
        break
    if my_list[log] > 0:
        print(my_list[log])
    log += 1
