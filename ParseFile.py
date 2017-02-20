import os
import collections


def parse(path):
    print("parse function")
    lists, count = getfile(path)
    data = get_data(lists)
    word_in_this_fold, word_set = calculate_the_number_of_word_in_this_set(data)
    return word_in_this_fold, word_set, count


def test_parse(path):
    print("test parse")
    lists, count = getfile(path)
    data = get_data(lists)
    return data


def getfile(path):
    count = 0
    lists = []
    for filename in os.listdir(path):
        filename_path = os.path.join(path, filename)
        if not filename.startswith('.') and os.path.isfile(filename_path):
            lists.append(filename_path)
            count += 1
    return lists, count


def get_data(lists):
    data = []
    for file in lists:
        with open(file, 'r', encoding='utf-8', errors='ignore') as file_read:
            d = file_read.read()
            data.append(d)
    return data


def calculate_the_number_of_word_in_this_set(data):
    word_in_this_fold = []
    for text in data:
        words_in_text = text.split()
        for word in words_in_text:
            if len(word) <= 1 or word == 'Subject:':
                continue
            word_in_this_fold.append(word)
    word_set = collections.Counter(word_in_this_fold)
    return word_in_this_fold, word_set



