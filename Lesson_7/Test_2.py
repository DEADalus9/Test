#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 12:45:43 2020

@author: vladislav

GRASSHOPER 3 MOVES +1, +2, *3
"""

def grpopper(n):
    
    gh = [0, 1] + [0] * (n - 1)
    
    for i in range(2, n + 1):
        gh[i] = gh[i - 2] + gh[i - 1] + gh[i // 3]
    
    print('gh = ', gh)    

    return gh[n]

    
print(grpopper(10))