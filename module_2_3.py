my_list =  [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

index = 0
quan = len(my_list)

while quan > index:
    a = my_list[index]
    if a > 0:
        print(a)
    elif a == 0:
        index = index + 1
        continue
    else:
        break
    index = index + 1
