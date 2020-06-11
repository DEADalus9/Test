#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 18:14:24 2020

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

sum_val = 0
for i in range(len(t)):
    sum_val += t[i]

print(sum_val)
