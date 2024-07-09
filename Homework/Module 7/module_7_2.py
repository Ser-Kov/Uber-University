def custom_write(file_name, strings):
    strings_positions = {}
    for i in strings:
        file = open(file_name, 'a', encoding='utf-8')
        tell = file.tell()
        file.write(i + '\n')
        file = open(file_name, 'r', encoding='utf-8')
        list_ = file.readlines()
        strings_positions[(list_.index(i + '\n') + 1, tell)] = i
    return strings_positions

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('test.txt', info)
for elem in result.items():
  print(elem)