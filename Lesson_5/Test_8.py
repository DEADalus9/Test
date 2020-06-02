#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 12:19:07 2020

@author: vladislav

DRAGON SPLINE
"""

import turtle

def dragon(l, n, dr):
    
    if n == 0:
        print('Zero level')
        turtle.forward((l ** 2 / 2) ** 0.5)
        return

    print('First turn right')
    if dr == 'right':
        turtle.right(45)
    else:
        turtle.left(45)
        
    print('First dragon')
    dragon(l, n - 1, 'right')  
    
    if dr == 'left':
        turtle.right(90)
    else:
        turtle.left(90)

    print('Second dragon')
    dragon(l, n - 1, 'left')
    
    if dr == 'right':
        turtle.right(45)
    else:
        turtle.left(45)


turtle.penup()
turtle.goto(-100, 0)
turtle.pendown()
turtle.speed('fastest')
dragon(20, 20, 'right')