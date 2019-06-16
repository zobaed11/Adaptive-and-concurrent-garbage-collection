#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 21 23:55:31 2018

@author: nsrg
@purpose: data merging
"""

import os
import sys
import pandas as pd

if __name__ == "__main__":
    
    
    final_data = pd.DataFrame(columns = ['prog_name','min_heap', 'init_heap', 'max_heap', 'gc_name'])
    
    
    ar= (16,32,48, 64, 96, 128, 160, 192, 224, 256, 512)
    allgcs=("UseParallelGC", "UseConcMarkSweepGC", "UseG1GC", "UseParNewGC", "UseSerialGC")
    directory = '/home/nsrg/Documents/Spring2018/OperatingSystems/Experiments/working_data/jolden_vm_data/'
    
    files = os.listdir(directory)
    
    min_heap = 0
    max_heap = 0
    init_heap = 0
    
    kk=0
    c=0
    for i in range(len(files)):
        
        data = pd.read_csv(directory+files[i], sep='\t')
        prog_name = files[i][7:files[i].index('.')]
        print("Starting for:", prog_name)
        for j in range (len (ar)): 
            min_heap= ar[j]
            for k in range (len (ar)): 
                max_heap= ar[k]
                for l in range(len(ar)):
                    init_heap=ar[l]
                    max_time=-1
                    storem = []
                    flag = 1
                    if l <= k:
                        for gc in allgcs:
                            algo = gc
                            
                            for m in range(len(data)):
                                if data.min_heap[m] == min_heap and data.max_heap[m] == max_heap and data.init_heap[m] == init_heap and data.gc_name[m]==algo:
                                    real_time = data.exec_time[m]
                                    #print('Hi', real_time)
                                    if real_time >=max_time:
                                        max_time = real_time
                                        storem.append(m)
                                        flag = 0
                                        
                        if flag ==0:
                            validm = max(storem)
                            final_data.loc[c] = [prog_name, data.iloc[validm].min_heap, data.iloc[validm].init_heap, data.iloc[validm].max_heap, data.iloc[validm].gc_name] 
                            c += 1

        print("Done for:", prog_name)
                                    
                            
                            
    
    
