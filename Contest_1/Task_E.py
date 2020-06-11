#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 17:38:36 2020

@author: vladislav
"""

n = int(input())
k = 0
z = 2
while z < n:
    z *= 2
    k += 1

print(k + 1)