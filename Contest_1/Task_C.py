#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 15 19:52:01 2020

@author: vladislav
"""
x = int(input())
if ((x % 4 == 0) and not (x % 100 == 0)) or (x % 400 == 0):
    print("YES")
else:    
    print("NO")