#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 16:17:47 2018

@author: nsrg
"""

import math
import os
import sys
import zlib

# define entropy
def H(data):
  if not data:
    return 0
  entropy = 0
  for x in range(256):
    p_x = float(data.count(chr(x)))/len(data)
    if p_x > 0:
      entropy += - p_x*math.log(p_x, 2)
      
  return entropy

# define complexity
def complexity(data):
    l=float(len(data))
    compr=zlib.compress(data)
    complexity=float(len(compr))/l
    
    return complexity


if __name__ == "__main__":
    
    
    
    files = ['mst', 'bh', 'voronoi', 'perimeter', 'power']
    
    write_to = open("jolden_statistics_data.txt", 'w')
    write_to.write('prog_name \t entropy \t complexity \n')
    for name in files:
        directory = '/home/nsrg/Documents/Spring2018/OperatingSystems/Experiments/working_data/jolden/'
        directory = directory + str(name) + str('/')
        #print(directory)
        all_files = os.listdir(directory)
        tot_ent = 0
        tot_complexity = 0
        for i in range(len(all_files)):
            content = str(open(str(directory)+all_files[i], 'rb').read())
            byteArr = bytearray(open(str(directory)+all_files[i], 'rb').read())
            tot_complexity += complexity(byteArr)
            tot_ent += H(content)
        avg_ent = tot_ent / len(all_files)
        avg_complexity = tot_complexity / len(all_files)
        write_to.write(str(name) + str("\t")+ str(avg_ent)+ str("\t") + str(avg_complexity) + str("\n"))
        
        
        
        
        