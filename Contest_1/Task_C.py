#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 15 19:52:01 2020

@author: vladislav
"""
N = 48500

if N % 4 == 0 or N % 400 == 0:
    print('YES')
elif N % 100 != 0:
   print('NO')