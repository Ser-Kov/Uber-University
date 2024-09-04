calls = 0

def count_calls():
    global calls
    calls += 1


def string_info(string):
    count_calls()
    return (len(string), string.upper(), string.lower())


def is_contains(string, list_to_search):
    count_calls()
    string_ = string.lower()
    list_to_search_update = []
    for i in list_to_search:
        i = i.lower()
        list_to_search_update.append(i)
    return string_ in list_to_search_update


print(string_info('Capybara'))
print(string_info('Armageddon'))
print(is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])) # Urban ~ urBAN
print(is_contains('cycle', ['recycling', 'cyclic'])) # No matches
print(calls)