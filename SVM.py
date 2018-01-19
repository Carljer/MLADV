import numpy as np
import random, math
import pylab
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits
from sklearn.svm import SVC
from sklearn.utils import shuffle
import pandas as pd
from sklearn.metrics import average_precision_score
from sklearn.metrics import recall_score
# from sklearn.metrics import zero_one_score


def kernel(v1,v2):
    numerator = np.dot(v1, v2)
    denominator = np.sqrt(np.dot(v1,v1) * np.dot(v2,v2))
    res = numerator / denominator
    return res

def svm(X_train, Y_train, X_test, Y_test):

    svc = SVC(kernel='precomputed')

    svc.fit(X_train, Y_train)
    Y_pred = svc.predict(X_test)
    Y_score = svc.decision_function(X_test)
    
    TF_mat = (Y_pred == Y_test)
#     print(Y_pred)
#     print(Y_test)
    true_pos = len([x for x in TF_mat if x==True])
    
    precision = average_precision_score(Y_test, Y_score)
#     recall = recall_score(Y_test, Y_pred, average='micro') 
    recall = recall_score(Y_test, Y_pred, average='weighted') 
#     print('precision: ', precision) 
#     print('recall', recall)
    return precision, recall 
