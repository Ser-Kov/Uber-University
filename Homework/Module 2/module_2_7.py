def print_params(a=1, b='строка', c=True):
    print(a, b, c)

# 1
print_params(13, 'не строка', (1, 3, 2))
print_params(b='число')
print_params()
print_params(b = 25)
print_params(c = [1,2,3])
# 2
values_list = ['Привет, я строка', 43, ['Kuban']]
values_dict = {'a': 'изменил аргумент "а"', 'b': 333, 'c': False}
print_params(*values_list)
print_params(**values_dict)
# 3
values_list_2 = [0, 'чудо']
print_params(*values_list_2, 42)  # Работает
