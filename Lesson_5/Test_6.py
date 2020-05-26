#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 26 18:27:02 2020

@author: vladislav

MINKOVSKI SPLINE
"""

import turtle

def minkovski(l, n):
    if n == 0:
        turtle.forward(l)

        return
   
    l = l // 8
    minkovski(l, n - 1)
    turtle.left(90)
    minkovski(l, n - 1)
    turtle.right(90)
    minkovski(l, n - 1)
    turtle.right(90)
    minkovski(l, n - 1)
    minkovski(l, n - 1)
    turtle.left(90)
    minkovski(l, n - 1)
    turtle.left(90)
    minkovski(l, n - 1)
    turtle.right(90)
    minkovski(l, n - 1)
    
turtle.penup()
turtle.goto(-300, 0)
turtle.pendown()
turtle.speed('fastest')
minkovski(8000, 4)


