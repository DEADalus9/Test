#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 26 22:14:52 2020

@author: vladislav

LEVI SPLINE
"""

import turtle

def levi(l, n):
    if n == 0:
        print('Zero level')
        turtle.forward(l)
        return
    
    print("Round {} in".format(n))
    
    turtle.left(45)
    print("First levi")
    levi(l, n - 1) 
    turtle.right(90)
    print("Second levi")
    levi(l, n - 1)
    turtle.left(45)
    print("Round {} out".format(n))
        
turtle.penup()
turtle.goto(-100, 0)
turtle.pendown()
turtle.speed('fastest')
levi(5, 12)


