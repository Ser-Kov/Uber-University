import re


class WordsFinder:
    def __init__(self, file_names):
        self.file_names = [file_names]

    def get_all_words(self):
        all_words = {}
        values_words = []
        for i in list(self.file_names):
            with open(i, encoding='utf-8') as file:
                lines = file.readlines()
                for line in lines:
                    text = line.lower()
                    new_text = re.sub("[,.=!?;:-]", '', text)
                    words = new_text.split()
                    values_words.extend(words)
                all_words[i] = values_words
        return all_words

    def find(self, word):
        word = word.lower()
        result_dict = {}
        for key, value in self.get_all_words().items():
            positions = []
            for index, name in enumerate(value):
                if word == name:
                    positions.append(index + 1)
            result_dict[key] = positions
        return result_dict

    def count(self, word):
        word = word.lower()
        result_dict = {}
        for key, value in self.get_all_words().items():
            count = 0
            for i in value:
                if word == i:
                    count += 1
            result_dict[key] = count
        return result_dict
