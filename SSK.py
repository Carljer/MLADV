import itertools
import pandas as pd
import numpy as np
pd.set_option('display.max_rows', 1000)
from SVM import *

def feature_mapping_of_substring(s, k):
    return [''.join(x) for x in itertools.combinations(s,k)]

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
    decay = 0.9
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
# 
# def get_phi_matrix(feature_space,doc, category):
#     phi_mat = []
# #     phi_mat_helper = []
#     for doc in docs:
# #         phi_mat_helper.append(getPhi_helper(feature_space, doc))
#         phi_mat.append(getPhi(feature_space, doc, category))
#     return phi_mat

def kernel(phi_mat):
    numerator = np.dot(phi_mat[0], phi_mat[1])
    denominator = np.sqrt(np.dot(phi_mat[0],phi_mat[0]) * np.dot(phi_mat[1],phi_mat[1]))
    res = numerator / denominator
    return res

def get_feature_space(docs,k):
    feature_space = []
    for doc in docs:
        a = feature_mapping_of_substring(doc, k)
        feature_space = feature_space + a
    return set(feature_space)

def start_string_kernel(k, docs, feature_space):
    class_A = []
    class_B = []
    cat_1 = []
    cat_2 = []
    for i in range(len(docs)):
#         print(docs[i])
        if docs[i][1] == 'earn':
            cat_1.append(docs[i][0])
        elif docs[i][1] == 'acq':
            cat_2.append(docs[i][0])

    cat1_matrix = pd.DataFrame([[None] * len(cat_1)]*len(cat_1))
    cat2_matrix = pd.DataFrame([[None] * len(cat_2)]*len(cat_2))
    for doc in cat_1:
        class_A.append(getPhi(feature_space, doc, 1))
    
    for doc in cat_2:
        class_B.append(getPhi(feature_space, doc , -1))
    
    data = class_A + class_B
    print(data)
    svm(data)
#         print(cat2_matrix)
# 
#     earn_classification = pd.DataFrame()
#     earn_classification['means_earn'] = cat1_matrix.mean(axis=1)
#     earn_classification['means_acq'] = cat2_matrix.mean(axis=1)
# #     print(cat_1_means)
# #     print(cat_2_means)
#     earn_classification['class'] =  earn_classification['means_earn'] >= earn_classification['means_acq']
#     earn_true_positives = len(earn_classification[earn_classification['class'] == True])
#     earn_false_positives = len(earn_classification[earn_classification['class'] == False])
# #     print(earn_positives)
#     print(earn_classification)
# 
# 
#     cat1_matrix = pd.DataFrame([[None] * len(cat_2)]*len(cat_2))
#     cat2_matrix = pd.DataFrame([[None] * len(cat_1)]*len(cat_2))
#     for i in range(len(cat_2)):
#         d1 = cat_2[i]
#         for j in range(len(cat_2)):
#             d2 = cat_2[j]
#             phi_mat = get_phi_matrix(feature_space, [d1,d2])
#             cat1_matrix[j][i] = kernel(phi_mat)
#         print(cat1_matrix)
#     for i in range(len(cat_2)):
#         d1 = cat_2[i]
#         for j in range(len(cat_1)):
#             d2 = cat_1[j]
#             phi_mat = get_phi_matrix(feature_space, [d1,d2])
#             cat2_matrix[j][i] = kernel(phi_mat)
# #         print(cat2_matrix)
# 
# 
# #         print(cat2_matrix)
#     acq_classification = pd.DataFrame()
#     acq_classification['means_earn'] = cat1_matrix.mean(axis=1)
#     acq_classification['means_acq'] = cat2_matrix.mean(axis=1)
# #     print(cat_1_means)
# #     print(cat_2_means)
#     acq_classification['class'] =  acq_classification['means_earn'] <= acq_classification['means_acq']
#     acq_positives = len(acq_classification[acq_classification['class'] == True])
#     acq_negatives = len(acq_classification[acq_classification['class'] == False])
#     print(acq_positives)
#     print(acq_negatives)
#     print(earn_true_positives)
#     print(earn_false_positives)
# 
#     precision = earn_true_positives / (earn_true_positives + earn_false_positives)
#     print('precision:',precision)
#     recall = earn_positives / (earn_positives + earn_negatives)
#     print('recall:',recall)
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


