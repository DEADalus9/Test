#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 12:32:24 2020

@author: vladislav

GRASSHOPER 3 MOVES +1, +2, +3
"""

def ghopper(n):
    gh = [0, 1, 2] + [0] * n
    
    for i in range(3, n + 1):
        gh[i] = gh[i - 3] + gh[i - 2] + gh[i - 1]
    
    return gh[n]

print(ghopper(3))