#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 18:21:42 2020

@author: vladislav
"""

t = []

while True:
    i = int(input())
    if i == 0:
        break
    else:
        t.append(i)
        continue
    
maximum = max(t)

k = 0
for i in t:
    if i == maximum:
        k += 1

print(k)
    
