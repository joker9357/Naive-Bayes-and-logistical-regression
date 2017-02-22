# -*- coding: utf-8 -*-
from ParseFile import parse, test_vector
from Naive_Bayes import accuracy
from Logistical_Regression import preprocess, logic_accuracy
from ParseStopWord import cut_the_stop_word, adjust_vector


def main():
    print("main function")
    spam_word, spam_word_set, spam_count, ham_word, ham_word_set, ham_count, attribute, input_vector, total_set, \
    spam_row, ham_row = parse('./3/train/spamtest', './3/train/hamtest')
    print("finish parse")
    naive_bayes_accuracy = accuracy(spam_count, spam_word, spam_word_set, ham_count, ham_word, ham_word_set, total_set)
    print("finish Naive_Bayes")
    weight_matrix = [0]*len(attribute)
    preprocess(input_vector, weight_matrix, 0.1, -10)
    test_matrix = test_vector(attribute, './3/test/spamtest', './3/test/hamtest')
    logistic_accuracy = logic_accuracy(weight_matrix, test_matrix)
    print(naive_bayes_accuracy, logistic_accuracy)
    stop_index, spam_cut, ham_cut = cut_the_stop_word(spam_word_set, ham_word_set, total_set, attribute)
    input_vector, test_matrix = adjust_vector(input_vector, test_matrix, stop_index)
    naive_bayes_without_stop_word=accuracy(spam_count, spam_word, spam_word_set, ham_count, ham_word, ham_word_set, total_set, spam_cut, ham_cut)
    weight_matrix = [0] * len(attribute)
    preprocess(input_vector, weight_matrix, 0.1, -10)
    logistic_without_stop_word_accuracy = logic_accuracy(weight_matrix, test_matrix)
    print("finish main")

    print(naive_bayes_without_stop_word, logistic_without_stop_word_accuracy)

if __name__ == "__main__": main()