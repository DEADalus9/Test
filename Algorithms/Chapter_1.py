#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 23 18:29:42 2020

@author: vladislav
BINARY SEARCH
"""

def binary_search(value, array):
   
    low = 0
    high = len(array) - 1
    
    while low <= high:
        middle = (high + low) // 2
        guess = array[middle]
        if guess == value:
            return middle
        if guess > value:
            high = middle - 1
        else:
            low = middle + 1
    return None

print(binary_search(5, [1, 2, 3, 4, 5, 6, 7]))

print(binary_search(0, [1, 2, 3, 4, 5, 6, 7]))


