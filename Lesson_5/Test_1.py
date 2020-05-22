#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 22 13:51:10 2020

@author: vladislav

FRACTAL
"""
import sys

k = 0

def fac(n):
    global k
    k += 1
    if n == 0:
        return 1
    else:
        return n * fac(n - 1)

print(fac(2955))

print(k)

print(sys.getrecursionlimit())


