#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 18:07:59 2020

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

max_val = t[0]
for i in range(len(t)):
    if t[i] > max_val:
        max_val = t[i]

print(max_val)

