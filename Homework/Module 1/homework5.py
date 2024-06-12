immutable_var = 15, 'Привет', [1, 2, 3], True
print(immutable_var)
immutable_var[0] = 20
print(immutable_var)
# Терминал выдает ошибку, потому что элементы кортежа невозможно изменить.
mutable_list = [2024, 'years', True]
print(mutable_list)
mutable_list[0] = 2000
mutable_list[1] = [20, 24]
mutable_list[2] = False
print(mutable_list)