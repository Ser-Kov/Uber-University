x = int(input('Введите первое число: '))
y = int(input('Введите второе число: '))
z = int(input('Введите третье число: '))
if x == y and x == z:
    print(3)
elif x == y or y == z:
    print(2)
else:
    print(0)