#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 18:35:09 2020

@author: vladislav
"""

a = [0] * 4

for i in range(4):
    a[i] = int(input())

if a[0] == a[2] or a[1] == a[3]:
    print('YES')
elif abs(a[2] - a[0]) ==  abs(a[3] - a[1]):
    print('YES')
else:
    print('NO')
