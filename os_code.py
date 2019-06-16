#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 24 15:00:45 2018

@author: c00300901
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score
import os
import numpy as np
import pandas as pd
import os
import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re
from nltk import stem

import sys
import numpy as np
from sklearn import preprocessing
import operator
from nltk.corpus import wordnet
from collections import defaultdict
import time
from sklearn.metrics.pairwise import cosine_similarity
import math

def cos_similarity(v1,v2):
    "compute cosine similarity of v1 to v2: (v1 dot v2)/{||v1||*||v2||)"
    sumxx, sumxy, sumyy = 0, 0, 0
    for i in range(len(v1)):
        x = v1[i]; y = v2[i]
        sumxx += x*x
        sumyy += y*y
        sumxy += x*y
    return sumxy/math.sqrt(sumxx*sumyy)





#training_data = {'f1': [1, 2, 3, 1],'f2':[3,34,29,12], 'f3': [20, 10, 13, 4],
#                 'label': [1, 1, 0,0]}
#
#test_data ={'f1':[2, 15, 27, 3],'f2':[4,72,18, 13], 'f3': [18, 50, 3, 19]}



ori_train_data=pd.read_csv("classification_data.csv")
ori_train_data= ori_train_data.drop(['Unnamed: 0'], axis=1)
sys.exit()
               
#df_tr = pd.DataFrame(training_data)
#
#
#df_trm= df_tr.drop(['label'], axis=1)
#df_trm = np.array(df_trm)
#df_ts = np.array (pd.DataFrame(test_data))
 
#assigned_label=[]
#for i in range(len(df_ts)):
#    total_count_sim=[]
#    for j in range(len(df_trm)):
#        total_count_sim.append(cos_similarity(df_ts[j], df_trm[i]))
#    ite=0
#    label=[]
#    for k in total_count_sim:
#        
#        if k>=.5:
#            label.append(df_tr.iloc[ite]['label'])
#        ite+=1
#    if label.count(1) > label.count(0):
#        assigned_label.append(1)
#    else:
#        assigned_label.append(0)
 
 

ori_test_data= ori_train_data.sample(n=200)

ori_data_m= np.array( ori_train_data.drop(['gc_name'], axis=1))

ori_test_data_m= np.array( ori_test_data.drop(['gc_name'], axis=1))
           
        
assigned_label=[]
for i in range(len(ori_test_data_m)):
    total_count_sim=[]
    for j in range(len(ori_data_m)):
        total_count_sim.append(cos_similarity(ori_data_m[j], ori_test_data_m[i]))
    ite=0
    label=[]
    for k in total_count_sim:
        
        if k>=.5:
            label.append(ori_train_data.iloc[ite]['gc_name'])
        ite+=1

        
    if label.count(1) == max(label.count(1), label.count(2), label.count(3), label.count(4), label.count(0) ): 
        assigned_label.append(1)
    elif label.count(2) == max(label.count(1), label.count(2), label.count(3), label.count(4), label.count(0) ): 
        assigned_label.append(2)
    elif label.count(3) == max(label.count(1), label.count(2), label.count(3), label.count(4), label.count(0) ): 
        assigned_label.append(3)
    elif label.count(4) == max(label.count(1), label.count(2), label.count(3), label.count(4), label.count(0) ): 
        assigned_label.append(4)
    else:
        assigned_label.append(0)
           
    sys.exit()
        
        
        
        
        
        
        
        
        
