# -*- coding: utf-8 -*-
from ParseFile import parse
from Naive_Bayes import accuracy

def main():
    print("main function")
    spam_word, spam_word_set, spam_count = parse('./train/spamtest')
    ham_word, ham_word_set, ham_count = parse('./train/hamtest')
    print("finish parse")
    accuracy(spam_count, spam_word, spam_word_set, ham_count, ham_word, ham_word_set)
    print("finish main")

if __name__ == "__main__": main()