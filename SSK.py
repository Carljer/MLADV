import itertools
import pandas as pd
import numpy as np
from SVM import *
# np.random.seed(100)

# 
# def feature_mapping_of_substring(s, k):
#     return [''.join(x) for x in itertools.combinations(s,k)]
# 
def getPhi(feature_space, doc, category):
    weight_vec = [None]*len(feature_space)
    i=0
    for feature in feature_space:
        length = get_weight_decay(feature, doc)
        weight_vec[i] = length
        i+=1
    return (category,weight_vec)

def get_weight_decay(feature, doc):
    length_counter = 0
    i = 0
    j = 0
    substr=''
    decay = 0.5
    while i < len(feature):
        while j < len(doc) and i < len(feature):
            if feature[i] not in doc:
                return 0
            if doc[j] == feature[i]:
                substr += doc[j]
                length_counter += 1
                i += 1
            elif len(substr) > 0:
                length_counter+=1
            j+=1
            if substr == feature:
                return decay ** length_counter
        j=0
        i+=1
    return 0

def createGram(train, test=None):
    if test == None:
        test=train
    G = np.zeros([len(train),len(test)]) # Init NxN matrix.
    for i in range(0, len(train)):
        for j in range(0, len(test)):
            G[i,j] = float(kernel(train[i], test[j]))
    return G

def kernel(v1,v2):
    numerator = np.dot(v1, v2)
    denominator = np.sqrt(np.dot(v1,v1) * np.dot(v2,v2))
    res = numerator / denominator
    return res
# 
# def get_feature_space(docs,k):
#     feature_space = []
#     for doc in docs:
#         a = feature_mapping_of_substring(doc, k)
#         feature_space = feature_space + a
#     return set(feature_space)
# 
def start_string_kernel(k, docs, feature_space):

    class_A = []
    class_B = []
    cat_1 = []
    cat_2 = []
    for i in range(len(docs)):
        if docs[i][1] == 'earn':
            class_A.append(getPhi(feature_space, docs[i][0], 1))
        elif docs[i][1] == 'acq':
            class_B.append(getPhi(feature_space, docs[i][0], -1))
   
    data = class_A + class_B

    X , Y = shuffle([d[1] for d in data], [d[0] for d in data] ) 

    phi_train , phi_test = X[0 : int(len(data)*0.7)] , X[int(len(data)*0.7) : ]
    Y_train , Y_test = Y[0 : int(len(data)*0.7)] , Y[int(len(data)*0.7) : ]
    X_train = np.array(createGram(phi_train))
    X_test = np.array(createGram(phi_train,phi_test)).T
#     print(X_train.shape)
#     print(X_test.shape)

    precision , recall = svm(X_train, Y_train, X_test, Y_test)
    print('precision: ', precision)
    print('recall: ', recall)
    return 0



















# def getPhi_helper(feature_space, doc):
#     weight_vec = [None]*len(feature_space)
#     i=0
#     for feature in feature_space:
#         length = get_weight_decay_helper(feature, doc)
#         weight_vec[i] = length
#         i+=1
#     return weight_vec
#
# def weight_decay_helper(feature, doc):
#     i = 0
#     seq_start = 0
#     decay = 0.5
#     if feature[0] not in doc:
#         return 0
#     while i < len(doc):
#         if doc[i] == feature[0]:
#             seq_start = i + 1
#             break
#         i += 1
#     return decay ** (len(doc) - i_start + 1)


