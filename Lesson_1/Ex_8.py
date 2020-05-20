#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 12 19:28:05 2020

@author: vladislav
"""

import turtle

def rectangular_helix(n, length):
    delta  = int(length * 1.0)

    for i in range(2 * n):
        turtle.forward(length + delta * i)
        turtle.left(90)
        turtle.forward(length + delta * i)
        turtle.left(90)
        
turtle.shape('turtle')

rectangular_helix(10, 10)