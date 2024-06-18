result_list = []


def check_int_or_str(value):
    if isinstance(value, int):
        result_list.append(value)
    elif isinstance(value, str):
        result_list.append(len(value))
    else:
        isinstance_check(value)


def for_list(list_):
    for elements_list in list_:
        check_int_or_str(elements_list)


def for_tuple(tuple_):
    for elements_tuple in tuple_:
        check_int_or_str(elements_tuple)


def for_set(set_):
    for elements_set in set_:
        check_int_or_str(elements_set)


def for_dict(dict_):
    for key, value in dict_.items():
        isinstance_check(key)
        isinstance_check(value)


def isinstance_check(value):
    if isinstance(value, list):
        for_list(value)
    elif isinstance(value, tuple):
        for_tuple(value)
    elif isinstance(value, set):
        for_set(value)
    elif isinstance(value, dict):
        for_dict(value)
    elif isinstance(value, int):
        result_list.append(value)
    elif isinstance(value, str):
        result_list.append(len(value))


def calculate_structure_sum(object_):
    for element in object_:
        isinstance_check(element)
    return sum(result_list)


data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
