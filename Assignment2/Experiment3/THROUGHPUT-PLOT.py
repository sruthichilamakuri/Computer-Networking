#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 27 17:35:02 2017

@author: sruthi
"""

import matplotlib.pyplot as plt
import numpy as np

"""  
CBR = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
TahoeLatency = [0.062924, 0.062926, 0.062919, 0.062959,  0.062982, 0.062965, 0.063292, 0.080410, 0.090918, 1.010050]
RenoLatency = [0.062924, 0.062926, 0.062919, 0.062959, 0.062982, 0.062965, 0.063292, 0.080410, 0.094381, 1.010050]
NewrenoLatency = [0.062924, 0.062926, 0.062919, 0.062959, 0.062982, 0.062965, 0.063292, 0.080410, 0.088100, 1.010050]
VegasLatency = [0.062799, 0.062862, 0.062864, 0.062869, 0.062777, 0.062943,  0.063263, 0.070239, 0.086521, 0.955145]
"""
"""
CBR = [ 7, 8, 9, 10]
TahoeLatency = [92.94, 72.83, 40.47, 3.70]
RenoLatency = [92.94, 72.83, 35.01, 3.70]
NewrenoLatency = [92.94, 72.83, 38.40, 3.70]
VegasLatency = [88.02, 70.85, 39.53, 2.58]
"""
"""
CBR = [ 8, 9, 10]
TahoeLatency = [ 0.080410, 0.090918, 1.010050]
RenoLatency = [ 0.080410, 0.094381, 1.010050]
NewrenoLatency = [ 0.080410, 0.088100, 1.010050]
VegasLatency = [ 0.070239, 0.086521, 0.955145]
"""
"""
CBR = np.array([ 8, 9, 10])
TahoeLatency = np.array([ 80410, 90918, 1010050]) #sheet2
RenoLatency = np.array([ 80410, 94381, 1010050]) #sheet1
NewrenoLatency = np.array([ 80410, 88100, 1010050]) #sheet4
VegasLatency = np.array([ 70239,86521, 955145]) #sheet3
"""
"""
#Throughputr with from and to node and flow defined
CBR = [7, 8, 9, 10]
TahoeLatency = [2437.72, 1909.62, 1059.92, 95.56]
RenoLatency = [ 2437.72, 1909.62, 916.69, 95.56]
NewrenoLatency = [ 2437.72, 1909.62, 1005.76, 95.56]
VegasLatency = [ 2222.39, 1788.77, 997.98, 64.69]
"""
X1 = [0.030096, 0.530832, 1.031568, 1.532304, 2.033264, 2.503664, 3.034960, 3.537136, 4.006800, 4.500400, 5.000304, 5.029936]  
X2 = [2.032400, 2.034032, 2.035664, 2.037296, 2.038928, 2.500400, 3.000496, 3.500272, 4.000336, 4.059728]
X3 = [0.030096, 0.530832, 1.031568, 1.532304, 2.033264, 2.502672, 3.006597, 3.519426, 4.003202, 4.503938, 5.004674, 5.016802]
X4 = [2.032400, 2.034032, 2.035664, 2.037296, 2.038928, 2.500208, 3.000400, 3.500162, 4.000738, 4.032098]




Y1 = [0.000000, 93640.000000, 260040.000000, 426440.000000, 592840.000000, 696840.000000, 751960.000000, 822680.000000, 876760.000000, 1001560.000000, 1166920.000000, 1183560.000000]
Y2 = [0.000000, 1000.000000, 2000.000000, 3000.000000, 4000.000000, 481000.000000, 1051000.000000, 1605000.000000, 2176000.000000, 2245000.000000]
Y3 = [0.000000, 93640.000000, 260040.000000, 426440.000000, 592840.000000, 664600.000000, 702040.000000, 763400.000000, 834120.000000, 937080.000000, 1093080.000000, 1103480.000000]
Y4 = [0.000000, 1000.000000, 2000.000000, 3000.000000, 4000.000000, 513000.000000, 1084000.000000, 1638000.000000, 2193000.000000, 2228000.000000]


plt.title("Throughput with SACK")
plt.xlabel('Time(seconds)')
plt.ylabel('Throughput (Kbps)')
droptailtcp, = plt.plot(X1,Y1,color='b',label='DropTail-tcp', alpha=1.0, marker = '*', linestyle='-.')
droptailcbr, = plt.plot(X2,Y2,color='g',label='DropTail-cbr', alpha=0.5, marker = '*' , linestyle='-')
redtcp, = plt.plot(X3,Y3,color='y',label='RED-tcp', alpha=1.0, marker = 's', linestyle=':')
redcbr, = plt.plot(X4,Y4,color='r',label='RED-cbr', alpha=0.5, marker = '+', linestyle='--')
plt.legend(handles=[droptailtcp,droptailcbr,redtcp,redcbr])

plt.show()