#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 11 18:27:41 2020

@author: vladislav
"""

n = int(input())

y = 1

while y ** 2 <= n:
    print(y ** 2, end = ' ')
    y += 1
    
