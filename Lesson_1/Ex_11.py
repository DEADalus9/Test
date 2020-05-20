#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 12 19:28:05 2020

@author: vladislav
"""

import turtle


def circle_left(n):
    for i in range(360):
        turtle.forward(n)
        turtle.left(1)
        
def circle_right(n):
    for i in range(360):
        turtle.forward(n)
        turtle.right(1)


def flower(m):
    n = 1
    for i in range(m):
        circle_left(n)
        circle_right(n)
        n += 0.1
   
turtle.shape('turtle')
turtle.left(90)
flower(5)