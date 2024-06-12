my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
count = 0
while count < len(my_list):
    if my_list[count] > 0:
        print(my_list[count])
        count += 1
    elif my_list[count] == 0:
        count += 1
        continue
    elif my_list[count] < 0:
        break
