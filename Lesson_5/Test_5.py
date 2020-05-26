#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 22 18:29:58 2020

@author: vladislav

KOCH STAR
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

def koch_star(l, n):
    for i in range(3):
        koch(l, n)
        turtle.right(120)

turtle.penup()
turtle.goto(-100, 0)
turtle.pendown()
koch_star(300, 4)