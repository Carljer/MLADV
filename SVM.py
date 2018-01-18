from cvxopt.solvers import qp
from cvxopt.base import matrix
from cvxopt import spmatrix
import numpy as np
import random, math
import pylab
import matplotlib.pyplot as plt

random.seed(100)
N = 0

def createP(data):
    P = [None] * len(data) # Init NxN matrix.
    for i in range(0, len(data)):
        P[i] = [None] * len(data)
        for j in range(0, len(data)):
            P[i][j] = float(data[i][0] * data[j][0] * kernel(data[i][1], data[j][1]))
#             print(data[i], data[j])
    return P

def createQ(data):
    q = matrix(-1.0, (len(data), 1) ) 
    return q

def createG(data, slack):
    if slack == True:
        G = matrix( np.concatenate( (np.diag([-1.0]*len(data)), np.diag([1.0]*len(data)) ), axis=0))
    else:
       G = matrix(np.diag([-1.0]*len(data)))
    return G
    
def createH(data, *args):
    if args:
        C = args[0]
        h = matrix( np.concatenate( ( [0.0] * len(data)  , [1.0*C]*len(data) ), axis=0) ) 
    else:
        h = matrix(0.0, (len(data), 1) ) 
    return h

def createAlpha(P,q,G,h, slack):
    global C
    res = qp(P, q, G, h)
    alpha = list(res['x'])
    alpha = [(i,x) for i,x in enumerate(alpha) if x > 0.00001]
    if slack:
        alpha = [(i,x) for i,x in alpha if x <= C]

    return alpha

def indicatorFunc(coordinate,data,alpha):
    pred=0.0
    for i,a_i in alpha:
        pred = pred + (a_i*data[i][0] * kernel(coordinate, data[i][1])) # 0:2=class, i=data_tuple
    return pred
 
def kernel(v1,v2):
    numerator = np.dot(v1, v2)
    denominator = np.sqrt(np.dot(v1,v1) * np.dot(v2,v2))
    res = numerator / denominator
    return res

def svm(data):
    
    global N 
    N = len(data)
    P = createP(data)
    print(data)
    
    q = createQ(data)
    slack = True# or slack = True 
    global C
    C = 100000 # C = 10 # C = 0.00001
    # Large values of C gives smaller margins and increases the complexity of the model,possible overfitting.
    # Small values of C makes the classifier ’sloppy’. It doesnt care if some points are misclassified. 
    if slack:
        G = createG(data, slack)
        h = createH(data,C)
    else:
        G = createG(data, slack = False)
        h = createH(data)
    alpha = createAlpha(matrix(P), q, matrix(G), matrix(h), slack)
    print(alpha)
#    countours
    xrange = np.arange(-4, 4, 0.05)
    yrange = np.arange(-4, 4, 0.05)
# 
#     pylab.hold(True)
# # 
    grid = matrix([[indicatorFunc(yd[1], data, alpha) for yd in data]])
    print(grid)
#   pylab.contour(xrange, yrange, grid,(-1,0,1), colors=('red', 'black', 'blue'),linewidths=(1,3,1))
# #         
    pylab.plot( [p for p in grid if p >0] ,'ro')
    pylab.plot( [p for p in grid if p <0] ,'bo')
#     pylab.plot( [p[0] for p in classB], [p[1] for p in classB],'bo')
#     
#     # plot the supportvector points.
#     for a in alpha:
#         pylab.plot(data[a[0]][0], data[a[0]][1], 'w+')
#         
    pylab.show()
