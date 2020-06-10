#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 14:07:54 2020

@author: vladislav

QWEEN GAME
"""

import numpy as np

def qg(m, n):
    
    F = [[False] * n for i in range(m)]
    
    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            if not F[i][j]:
                F[i][j] = False
                for k in range(1, max(m, n)):
                    if i - k >= 0:
                        F[i - k][j] = True
                    if j - k >= 0:
                        F[i][j - k] = True
                    if i - k >= 0 and j - k > 0:
                        F[i - k][j - k] = True
        
    a = np.array(F)
    print(a)
    print('First position', F[0][0])
 

qg(4, 3)