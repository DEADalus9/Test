#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 17:52:08 2020

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

k = 0
for el in t:
    if not el % 2:
        k += 1
        
print(k)