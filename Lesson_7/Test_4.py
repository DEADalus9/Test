#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  9 16:03:25 2020

@author: vladislav

GRASSHOPER WITH TRAJECTORY
"""

# Steps
n = 5

def grhopper(n):
    gh = [0] * (n + 1)
    gh[0] = 0
    gh[1] = 1    
    for i in range(2, n + 1):
        gh[i] = gh[i - 2] + gh[i - 1]
    
    return gh[n]

print('Amount of possibilities:', grhopper(n))

def calculate_min_cost(n, price):
    
    gh_cost = [price[0], price[1]] + [0] * (n - 1)
    prev = [0] * (n + 1)
    prev[1] = 0
    for i in range(2, n + 1):
        gh_cost[i] = price[i] + min(gh_cost[i - 1], gh_cost[i - 2])
        if gh_cost[i - 1] < gh_cost[i - 2]:
            prev[i] = i - 1
        else:
            prev[i] = i - 2
    
    print('Total mimimal price:' , gh_cost[n])
    
    path = []
    i = n
    while i > 0:
        path.append(i)
        i = prev[i]
    path.append(0)
    path = path[::-1]
    print('path =', path)


        #1 #2 #3 #4 #5 #6 #7 #8 #9#10#11#12#13#14 
price = [0, 2, 5, 2, 5, 2, 5, 2, 5, 2, 5, 2, 5, 2]

calculate_min_cost(n, price)
