import collections


def parse_stop_word():
    path = './STOP_WORDS.txt'
    with open(path, 'r', encoding='utf-8', errors='ignore') as file_read:
        d = file_read.read()

    data = d.split()
    return data
    print("finish parse stop word")


def cut_the_stop_word(spam_word_set, ham_word_set, total_set, attribute):
    data = parse_stop_word()
    # data = ['ello2', 'hello3']
    spam_cut = 0
    ham_cut = 0
    stop_index = []
    for word in data:
        if word in spam_word_set:
            spam_cut +=  spam_word_set[word]
            del spam_word_set[word]

        if word in ham_word_set:
            ham_cut +=  ham_word_set[word]
            del ham_word_set[word]

        if word in total_set:
            del total_set[word]
            index = attribute.index(word)
            stop_index += [index]
            del attribute[index]

    return stop_index, spam_cut, ham_cut
    print("finish cut")


def adjust_vector(input_matrix, test_matrix, stop_index):
    for input_vector in input_matrix:
        for index in stop_index:
            del input_vector[index+1]

    for test_vector in test_matrix:
        for index in stop_index:
            del test_vector[index+1]

    return input_matrix, test_matrix