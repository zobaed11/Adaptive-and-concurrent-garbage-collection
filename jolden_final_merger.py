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
import pandas as pd

def static_formatter():
    
    prog_name = ['mst', 'bh', 'voronoi', 'perimeter', 'power']
    

    

    

    c=0
    dit = 0
    wmc = 0
    noc = 0
    cbo = 0
    rfc = 0
    lcom = 0
    ca = 0
    npm = 0
    
    for i in range(len(static)):
        
        if static.prog_name[i].startswith('power'):
            
            c+=1
            dit += static.dit[i]
            wmc += static.wmc[i]
            noc += static.noc[i]
            cbo += static.cbo[i]
            rfc += static.rfc[i]
            lcom += static.lcom[i]
            ca += static.ca[i]
            npm += static.npm[i]
            
    avg_dit = dit / c
    avg_wmc = wmc / c
    avg_noc = noc / c
    avg_cbo = cbo / c
    avg_rfc = rfc / c
    avg_lcom = lcom / c
    avg_ca = ca / c
    avg_npm = npm / c
        
    with open("power_info.txt" , "w") as f:
        f.write(str(avg_dit)+ "\t" + str(avg_wmc)+ "\t" + str( avg_noc )+"\t" + str(avg_cbo)+ "\t" + str(avg_rfc)+ "\t" +
                str(avg_lcom)+"\t" + str(avg_ca)+"\t" + str(avg_npm)+ "\t" )


if __name__ == "__main__":
    
    statistics_data = pd.read_csv('jolden_statistics_data.txt', sep='\t')
    statistics_data['index']=range(len(statistics_data))
    static_power = pd.read_csv('power_info.txt', sep='\t')
    static_bh = pd.read_csv('bh_info.txt', sep='\t')
    static_mst = pd.read_csv('mst_info.txt', sep='\t')
    static_voronoi = pd.read_csv('voronoi_info.txt', sep='\t')
    static_perimeter = pd.read_csv('perimeter_info.txt', sep='\t')
    dynamic_vm = pd.read_csv('jolden_dynamic_data.txt', sep='    ')
    
    
    final_data = pd.DataFrame(columns = ['prog_name','entropy', 'complexity','dit', 'wmc', 'noc', 'cbo', 'rfc', 'lcom', 'ca', 'npm','min_heap', 'init_heap', 'max_heap', 'gc_name'])
    
    dynamic_vm['entropy'] = 0.0
    dynamic_vm['complexity'] = 0.0
    for i in range(len(dynamic_vm)):
        
        if dynamic_vm.prog_name[i] == 'bh':
            dynamic_vm['entropy'][i] = statistics_data.loc[1][1]
            dynamic_vm['complexity'][i] = statistics_data.loc[1][2]
            

    

        
        
    
    
    
    
        
        
        
        