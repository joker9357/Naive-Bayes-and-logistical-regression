import math
from ParseFile import test_parse


def training(spam_count, spam_word, spam_word_set, ham_count, ham_word, ham_word_set):

    spam_prior = math.log(1.0*spam_count/(spam_count+ham_count), 2)
    ham_prior = math.log(1.0*ham_count/(spam_count+ham_count), 2)
    spam_length = len(spam_word)
    ham_length = len(ham_word)
    total_length = len(spam_word_set+ham_word_set)
    spam_dict = {}
    ham_dict = {}
    for i in spam_word_set:
        num = spam_word_set[i]
        p = 1.0*(num+1)/(spam_length+total_length)
        spam_dict[i] = math.log(p, 2)

    for i in ham_word_set:
        num = ham_word_set[i]
        p = 1.0*(num+1)/(ham_length+total_length)
        ham_dict[i] = math.log(p, 2)

    return spam_prior, ham_prior, spam_dict, ham_dict,total_length


def accuracy(spam_count, spam_word, spam_word_set, ham_count, ham_word, ham_word_set):
    success = 0#number of right file
    count = 0  #number of test file
    spam_prior, ham_prior, spam_dict, ham_dict, total_length = training(spam_count, spam_word, spam_word_set, ham_count, ham_word, ham_word_set)
    print("finish training")
    spam_data = test_parse('./test/spamtest')
    ham_data = test_parse('./test/spamtest')
    for i in spam_data:
        count+=1
        p_s = spam_prior
        p_h = ham_prior
        word = calculate_the_number_of_word(i)
        for j in range(len(word)):
            if word[j] in spam_dict:
                p_s += spam_dict[word[j]]
            else:
                p_s += 1.0*(math.log(1/(spam_count+total_length), 2))

            if word[j] in ham_dict:
                p_s += ham_dict[word[j]]
            else:
                p_s += 1.0*(math.log(1/(ham_count+total_length), 2))

        if p_s > p_h:
            success += 1

    for i in ham_data:
        count+=1
        p_s = spam_prior
        p_h = ham_prior
        word = calculate_the_number_of_word(i)
        for j in range(len(word)):
            if word[j] in spam_dict:
                p_s += spam_dict[word[j]]
            else:
                p_s += 1.0 * (math.log(1 / (spam_count + total_length), 2))

            if word[j] in ham_dict:
                p_s += ham_dict[word[j]]
            else:
                p_s += 1.0 * (math.log(1 / (ham_count + total_length), 2))

        if p_s < p_h:
            success += 1

    print("finish Navie Bayes")

    return 1.0*success/count



def calculate_the_number_of_word(data):
    word_in_this_fold = []
    words_in_text = data.split()
    for word in words_in_text:
        if len(word) <= 1 or word == 'Subject:':
            continue
        word_in_this_fold.append(word)

    return word_in_this_fold

