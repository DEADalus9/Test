#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 22 14:21:26 2020

@author: vladislav

KOCH SPLINE
"""

import turtle

def koch(l, n):
    if n == 0:
        turtle.forward(l)
        return
    
    x = l // 3
    koch(x, n - 1)
    turtle.left(60)
    koch(x, n - 1)
    turtle.right(120)
    koch(x, n - 1)
    turtle.left(60)
    koch(x, n - 1)
    #turtle.left(180)
    #turtle.forward(l)

turtle.penup()
turtle.goto(-100, 0)
turtle.pendown()
koch(300, 4)