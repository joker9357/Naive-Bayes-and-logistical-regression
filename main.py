# -*- coding: utf-8 -*-
from ParseFile import parse
from Naive_Bayes import accuracy
from Logistical_Regression import preprocess, logic_accuracy


def main():
    print("main function")
    spam_word, spam_word_set, spam_count, ham_word, ham_word_set, ham_count, attribute, input_vector = parse('./3/train/spamtest', './3/train/hamtest')
    print("finish parse")
    naive_bayes_accuracy = accuracy(spam_count, spam_word, spam_word_set, ham_count, ham_word, ham_word_set)
    print("finish Naive_Bayes")
    weight_matrix = [0]*len(attribute)
    preprocess(attribute, input_vector, weight_matrix, 0.1, -10)
    logistic_accuracy = logic_accuracy(weight_matrix)
    print("finish main")

if __name__ == "__main__": main()