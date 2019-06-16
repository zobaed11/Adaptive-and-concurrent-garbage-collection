#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 18 14:48:43 2017

@author: nsrg
"""

from sklearn.svm import SVC
from sklearn.naive_bayes import GaussianNB
from sklearn.multiclass import OneVsRestClassifier
from sklearn.preprocessing import LabelBinarizer
from sklearn.linear_model import LogisticRegression
import pandas as pd
import numpy as np
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report, hamming_loss
from sklearn.metrics import average_precision_score
from sklearn.metrics import precision_score, recall_score
import glob
from sklearn.model_selection import cross_val_score
from sklearn import svm
import warnings
from sklearn import preprocessing
import sys
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import f1_score
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn import tree
warnings.filterwarnings("ignore")
import numpy 
from sklearn.decomposition import NMF
from sklearn import metrics
from sklearn.neighbors.nearest_centroid import NearestCentroid
import matplotlib.pyplot as plt
from matplotlib import rc
from pylab import *
rcParams.update({'figure.autolayout': True})
from sklearn import preprocessing
from sklearn.preprocessing import StandardScaler

# these below lines are very important to match the fonts with actual latex fonts
plt.rc('text', usetex=True)
plt.rc('font', family='Times')

rc('text', usetex=True)

scaler=StandardScaler()

def matrix_factorization(R, P, Q, K, steps=5, alpha=0.0002, beta=0.02):
    Q = Q.T
    for step in range(steps):
        for i in range(len(R)):
            for j in range(len(R[i])):
                if R[i][j] > 0:
                    eij = R[i][j] - numpy.dot(P[i,:],Q[:,j])
                    for k in range(K):
                        P[i][k] = P[i][k] + alpha * (2 * eij * Q[k][j] - beta * P[i][k])
                        Q[k][j] = Q[k][j] + alpha * (2 * eij * P[i][k] - beta * Q[k][j])
        #eR = numpy.dot(P,Q)
        e = 0
        for i in range(len(R)):
            for j in range(len(R[i])):
                if R[i][j] > 0:
                    e = e + pow(R[i][j] - numpy.dot(P[i,:],Q[:,j]), 2)
                    for k in range(K):
                        e = e + (beta/2) * ( pow(P[i][k],2) + pow(Q[k][j],2) )
        if e < 0.001:
            break
    return P, Q.T

if __name__ == "__main__":
    
    labels = ['UseParallelGC', 'UseConcMarkSweepGC', 'UseG1GC', 'UseParNewGC', 'UseSerialGC']
    path = './classification_data_trial_2.csv'
    data = pd.read_csv(path)    
    data = data.drop(['Unnamed: 0'], axis=1)
    
    """
    this was used to convert the labels into numeric
    """
#    for i in range(len(data)):
#        if data.gc_name[i] == labels[0]:
#            data.gc_name[i] = 0
#        elif data.gc_name[i] == labels[1]:
#            data.gc_name[i] = 1
#        elif data.gc_name[i] == labels[2]:
#            data.gc_name[i] = 2
#        elif data.gc_name[i] == labels[3]:
#            data.gc_name[i] = 3
#        elif data.gc_name[i] == labels[4]:
#            data.gc_name[i] = 4
    
    class_column = np.array(data.gc_name)
    
    
    data_column = data.drop(['gc_name'], axis=1)
    data_column = np.array(data_column)
#    min_max_scaler = preprocessing.MinMaxScaler()
#    data_column=min_max_scaler.fit_transform(data_column)
    W = data_column
    N = len(data_column)
    M = len(data_column[0])
    K = min(M,N)   
    
    model = NMF(n_components=K, init='random', random_state=0)
    W = model.fit_transform(data_column)

    models = ['lr','lda','nb','mlp','svm']
    
    outfile = open('results_summary.txt', 'w')
    outfile.write(str('algorithm')+str('\t')+str('scores')+str('\n'))
    
    plt.figure(1)
    #plt.tight_layout()
    f, ax = plt.subplots(1)
    
    
    for k in range(len(models)):
        print("Computation going on for:", models[k])
        if models[k]=='lr':
            model = LogisticRegression()
            color = 'r-*'
        elif models[k]=='lda':
            model = LinearDiscriminantAnalysis()
            color = 'b-^'
        elif models[k]=='nb':
            model = GaussianNB()
            color = 'g-o'
        elif models[k]=='mlp':
            model = MLPClassifier(solver='sgd', alpha=1e-5, hidden_layer_sizes=(3, 2), random_state=1)
            color = 'k-<'
        elif models[k]=='tree':
            model = tree.DecisionTreeClassifier()
            color = 'c-x'
        else:
            model = svm.SVC(C=1.0, kernel='rbf', class_weight='balanced')
            color = 'm->'

        W = data_column
        sz = W.shape

        train = W[:int(sz[0] * 0.2)]
        test = W[int(sz[0] * 0.2):]

        y = class_column[:int(sz[0] * 0.2)]
        X = train
        
        test_Y = class_column[int(sz[0] * 0.2):]
        test_X = test
        
        model = model.fit(X, y)
        y_hat = model.predict(test_X)
        scores = cross_val_score(model, X, y, cv=10)
        dim = np.arange(len(scores))
        
               
        
        ax.plot(scores, color,mfc='none')
        #ax.tight_layout()
        
        #print ("Accuracy Rate, which is calculated by accuracy_score() is: %f" % accuracy_score(test_Y, y_hat))
        #print ("Hamming loss: ", hamming_loss(test_Y, y_hat))
        #print ("Average precision score:", precision_score(test_Y, y_hat, average='macro'))
        
        #print ("Confusion matrix:\n", confusion_matrix(test_Y, y_hat))
    ax.legend(['LR','LDA','NB','MLP','SVM'])
    ax.set_xlabel('Iteration')
    ax.set_ylabel('Precision')
    ax.set_xticks(dim)
    
#    plt.grid()
    
    
    plt.savefig('precision_old_dacapo.pdf')
#    plt.savefig('precision_old_dacapo_with_feature.pdf')
    plt.show()
    outfile.close()
         