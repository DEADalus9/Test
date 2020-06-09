#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 13:57:16 2020

@author: vladislav

GRASSHOPER +1 +2 WITH PRICE
"""

def grhopper(n):
    gh = [0, 1] + [0] * (n - 1)
    
    for i in range(2, n + 1):
        gh[i] = gh[i - 2] + gh[i - 1]
    
    return gh[n]

print(grhopper(3))

def calculate_min_cost(n, price):
    
    gh_cost = [0, price[1]] + [0] * (n - 1)
    for i in range(2, n + 1):
        gh_cost[i] = price[i] + min(gh_cost[i - 1], gh_cost[i - 2])
        
    return gh_cost[n]


price = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]

print(calculate_min_cost(10, price))

