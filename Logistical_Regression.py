import math


def preprocess(input_vector, weight_matrix, learning_rate, lambda_input):
    for iterator in range(2):
        gradient = []
        w0 = 0
        for vector in input_vector:
            sum_of_product = 0
            for i in range(1, len(vector)):
                sum_of_product=sum_of_product+weight_matrix[i-1]*vector[i]
            try:
                exp = math.exp(1.0*w0+sum_of_product)
                gradient.append(vector[0]-(exp/(1+exp)))
            except:
                gradient.append(vector[0] - 1)

        for j in range(len(weight_matrix)):
            sum_all = 0
            for i in range(len(input_vector)):
                sum_all = sum_all + input_vector[i][j+1]*gradient[i]
            weight_matrix[j] = weight_matrix[j]+(learning_rate*sum_all)-(learning_rate*lambda_input*weight_matrix[j])
    print("finish preprocess")
    return weight_matrix


def logic_accuracy(weight_matrix, test_matrix):
    success = 0
    count = 0
    for vector in test_matrix:
        count += 1
        sum_of_result = 0
        for i in range(1, len(vector)):
            sum_of_result += weight_matrix[i-1]*vector[i]

        if sum_of_result > 0 and vector[0] == 1:
            success += 1
        if sum_of_result < 0 and vector[0] == 0:
            success += 1

    return 1.0*success/count
    print("finish logic_accuracy")



