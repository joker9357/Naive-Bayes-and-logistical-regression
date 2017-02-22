import os
import collections



def parse(spam_path,ham_path):
    print("parse function")
    spam_lists, spam_count = getfile(spam_path)
    ham_lists, ham_count = getfile(ham_path)
    spam_data = get_data(spam_lists)
    ham_data = get_data(ham_lists)
    spam_word, spam_word_set, spam_row = calculate_the_number_of_word_in_this_set(spam_data)
    ham_word, ham_word_set, ham_row = calculate_the_number_of_word_in_this_set(ham_data)
    total_set = spam_word_set + ham_word_set
    attribute, input_vector = inputvector(spam_word, spam_row, ham_word, ham_row,total_set)
    return spam_word, spam_word_set, spam_count, ham_word, ham_word_set, ham_count, attribute, input_vector, total_set, \
           spam_row, ham_row


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
    row=[]
    word_in_this_fold = []
    for text in data:
        row.append(len(word_in_this_fold))
        words_in_text = text.split()
        for word in words_in_text:
            if len(word) <= 1 or word == 'Subject:':
                continue
            word_in_this_fold.append(word)
    word_set = collections.Counter(word_in_this_fold)
    return word_in_this_fold, word_set, row


def inputvector(spam_word, spam_row, ham_word, ham_row, total_set):
    attribute = list(total_set.keys())
    length = len(attribute)
    inputmatrix = []
    for i in range(len(spam_row)):
        if i+1 <= len(spam_row)-1:
            text = spam_word[spam_row[i]:spam_row[i+1]]
        else:
            text = spam_word[spam_row[i]:]
        text_counter = collections.Counter(text)
        vector = [0]*length
        for j in text_counter:
            if j not in attribute:
                continue
            attribute_index = attribute.index(j)
            vector[attribute_index] = text_counter[j]
        vector.insert(0, 0)
        inputmatrix.append(vector)

    for i in range(len(ham_row)):
        if i+1 <= len(ham_row)-1:
            text = ham_word[ham_row[i]:ham_row[i+1]]
        else:
            text = ham_word[ham_row[i]:]
        text_counter = collections.Counter(text)
        vector = [0]*length
        for j in text_counter:
            attribute_index = attribute.index(j)
            vector[attribute_index] = text_counter[j]
        vector.insert(0, 1)
        inputmatrix.append(vector)

    return attribute, inputmatrix


def test_vector(attribute, spam_path, ham_path):
    spam_lists, spam_count = getfile(spam_path)
    ham_lists, ham_count = getfile(ham_path)
    spam_data = get_data(spam_lists)
    ham_data = get_data(ham_lists)
    spam_word, spam_word_set, spam_row = calculate_the_number_of_word_in_this_set(spam_data)
    ham_word, ham_word_set, ham_row = calculate_the_number_of_word_in_this_set(ham_data)
    length = len(attribute)
    test_matrix = []
    for i in range(len(spam_row)):
        if i+1 <= len(spam_row)-1:
            text = spam_word[spam_row[i]:spam_row[i+1]]
        else:
            text = spam_word[spam_row[i]:]
        text_counter = collections.Counter(text)
        vector = [0]*length
        for j in text_counter:
            attribute_index = attribute.index(j)
            vector[attribute_index] = text_counter[j]
        vector.insert(0, 0)
        test_matrix.append(vector)

    for i in range(len(ham_row)):
        if i+1 <= len(ham_row)-1:
            text = ham_word[ham_row[i]:ham_row[i+1]]
        else:
            text = ham_word[ham_row[i]:]
        text_counter = collections.Counter(text)
        vector = [0]*length
        for j in text_counter:
            attribute_index = attribute.index(j)
            vector[attribute_index] = text_counter[j]
        vector.insert(0, 1)
        test_matrix.append(vector)

    return test_matrix







