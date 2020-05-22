#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 22 14:05:15 2020

@author: vladislav

FIBONACCHI
"""

def fib(n):
    """
    Fibonacchi number

    Parameters
    ----------
    n : INT
        Value to calculate.

    Returns
    -------
    INT
        Number of Fibonacchi.

    """
    
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

print(fib(10))



