import random
import time

first_column = random.randrange(3, 21)
print(f'Подберите пароль к числу: {first_column}')


def divider():
    i = 2
    dividers = []
    while i <= first_column:
        if first_column % i == 0:
            dividers.append(i)
        i += 1
    return dividers


def search_psw():
    print('Запущен процесс подбора паролей')
    password = []
    for i in divider():
        first_number = 1
        while first_number < i:
            second_number = i - first_number
            if first_number + second_number == i and first_number <= second_number:
                password.append(f'{first_number}{second_number}')
            else:
                break
            first_number += 1
    time.sleep(2)
    print('Почти готово...')
    time.sleep(3)
    print('Варианты паролей:', *password)
    return password


password = search_psw()
enter = int(input('Введите пароль: '))
count_attempts = 0
for i in password:
    count_attempts += 1
    if str(enter) == i:
        print('Пароль верный. Вы свободны!')
        break
    elif str(enter) != i:
        if count_attempts == len(password):
            print('Пароль неверный! Вы останетесь здесь навсегда!')
        else:
            continue
