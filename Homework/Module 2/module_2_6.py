def single_root_words(root_word, *other_words):
    same_words = []
    elements_0 = []
    elements_1 = []
    for i in str(root_word).lower():
        elements_0 += i
    for word in other_words:
        elements_1.clear()
        check = ''
        for j in str(word).lower():
                elements_1 += j
        for symbol_0 in elements_0:
            if len(check) == 3:
                if check in str(word).lower():
                    same_words.append(word)
                break
            for symbol_1 in elements_1:
                if symbol_0 == symbol_1:
                    check += symbol_1
                    break
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)