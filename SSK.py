import itertools
import numpy as np

def feature_mapping_of_substring(s, k):
    return [''.join(x) for x in itertools.combinations(s,k)]

def getPhi(feature_space, doc):
    weight_vec = [None]*len(feature_space)
    i=0
    for feature in feature_space:
        length = get_weight_decay(feature, doc)
        weight_vec[i] = length
        i+=1
    return weight_vec

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

def get_phi_matrix(feature_space,docs):
    phi_mat = []
    phi_mat_helper = []
    for doc in docs:
#         phi_mat_helper.append(getPhi_helper(feature_space, doc))
        phi_mat.append(getPhi(feature_space, doc))
    return phi_mat

def kernel(phi_mat,s,t):
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
#     s = "science is organized knowledge"
#     t = "wisdom is organized life"
#     docs = ['cat','car','bat', 'bar']
#     k = 2
#     docs = [s , t]
#     feature_space = get_feature_space(docs,k)
    phi_mat = get_phi_matrix(feature_space, docs)
    K = kernel(phi_mat,s,t)
    return K

# if __name__ == '__main__':
#     start_string_kernel()



















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


