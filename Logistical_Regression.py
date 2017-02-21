import math


def preprocess(attribute, input_vector, weight_matrix, learning_rate, lambda_input):
    for iterator in range(5):
        gradient = []
        w0 = 0
        for vector in input_vector:
            sum_of_product = 0
            for i in range(1, len(vector)):
                sum_of_product=sum_of_product+weight_matrix[i-1]*vector[i]
            exp = math.exp(1.0*w0+sum_of_product)
            gradient.append(vector[0]-(exp/(1+exp)))

        for j in range(len(weight_matrix)):
            sum_all = 0
            for i in range(len(input_vector)):
                sum_all = sum_all + input_vector[i][j+1]*gradient[i]
            weight_matrix[j] = weight_matrix[j]+(learning_rate*sum_all)-(learning_rate*lambda_input*weight_matrix[j])
    print("finish preprocess")
    return weight_matrix


def logic_accuracy(weight_matrix):

    print("finish logic_accuracy")



