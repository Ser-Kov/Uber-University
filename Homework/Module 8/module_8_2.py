def personal_sum(numbers):
    result = 0
    for i in numbers:
        result += i
    return result


def calculate_average(numbers):
    try:
        return personal_sum(numbers) / len(numbers)
    except ZeroDivisionError:
        return 0
    except TypeError:
        return 'В numbers записан некорректный тип данных'


print(f'Результат 1: {calculate_average("1, 2, 3")}')
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')
print(f'Результат 3: {calculate_average(567)}')
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')
