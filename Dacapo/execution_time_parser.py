#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 28 21:14:10 2018

@author: nsrg
"""
import sys
import os


global header_flag

global prog_name


def getProg(arg):
    file = open('/home/c00300901/Desktop/dacapo/script/raw_data/'+str(arg),'r')
    count = 0
    store = []
    for line in file:
        words=line.split()
        for word in words:
            if word.find("real=") != -1:
                word=word[5:]
                if (word != "0.00"):
                    store.append(float(word))
                count+=1   
    a=arg
    b=a.replace('_', ' ')
    ls = b.split()



    global prog_name
    prog_name = ls[1]
    
    return prog_name
    
    
def call_me(arg):
    file = open('/home/c00300901/Desktop/dacapo/script/raw_data/'+str(arg),'r')

    count = 0
    store = []
    for line in file:
        words=line.split()
        for word in words:
            if word.find("real=") != -1:
                word=word[5:]
                if (word != "0.00"):
                    store.append(float(word))
                count+=1   
    a=arg
    b=a.replace('_', ' ')
    ls = b.split()

    ac= ls[5]
    for i in range(len(ac)):
        if ac[i] == '.':
            ind=i
            
    min_heap = ac[:ind-1][3:]
    
    max_heap = ls[3][3:-1]
    init_heap =ls[4][3:-1]
    gc_name = ls[2]
    exec_time = max(store)
    global prog_name
    prog_name = ls[1]
    #print(prog_name)
    benchmark = "spec"

    outputfile_name = open(str(benchmark)+str("_")+str(prog_name)+'.txt','a')
    
    global header_flag
#    if(prog_name == "compiler"):
    if header_flag ==1:
        outputfile_name.write(str("benchmark"+"\t"+"max_heap"+"\t"+"init_heap"+"\t"+"min_heap"+"\t"+"gc_name"+"\t"+"exec_time"+"\n"))
        f = open("flag_file_" +str(prog_name)+ ".txt", 'w')
        f.write('0')
    
    outputfile_name.write(str(str(prog_name)+"\t"+str(max_heap)+"\t"+str(init_heap)+"\t"+str(min_heap)+"\t"+str(gc_name)+"\t"+str(exec_time)+str("\n")))
    
    
if __name__ == "__main__":

        
    
    prog_name = getProg(sys.argv[1])

    
    if (prog_name == "luindex"):     
        header_flag=0
        header_flag = int(open("flag_file_luindex.txt", 'r').read().strip())
        call_me(sys.argv[1])



    if (prog_name == "lusearch-fix"):     
        header_flag=0
        header_flag = int(open("flag_file_lusearch-fix.txt", 'r').read().strip())
        call_me(sys.argv[1])
        
        
    if (prog_name == "pmd"):     
        header_flag=0
        header_flag = int(open("flag_file_pmd.txt", 'r').read().strip())
        call_me(sys.argv[1])



    if (prog_name == "sunflow"):     
        header_flag=0
        header_flag = int(open("flag_file_sunflow.txt", 'r').read().strip())
        call_me(sys.argv[1])   
        
    
    if (prog_name == "tomcat"):     
        header_flag=0
        header_flag = int(open("flag_file_tomcat.txt", 'r').read().strip())
        call_me(sys.argv[1])



    if (prog_name == "jython"):     
        header_flag=0
        header_flag = int(open("flag_file_jython.txt", 'r').read().strip())
        call_me(sys.argv[1])
        
    
