#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 18:16:17 2020

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
for i in t:
    if i != 0:
        k += 1

print(k)
