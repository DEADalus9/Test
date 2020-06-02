#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  2 16:28:56 2020

@author: vladislav

KANTOROV PLANTY
"""

import turtle

def kantorov(l, n, x, y):
    if n == 0:
        turtle.forward(l)
        return

    turtle.forward(l)
  
    l /= 3
    y -= 10
    
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    
    kantorov(l, n - 1, x, y)
    
    x += 2 * l  
    
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    
    kantorov(l, n - 1, x, y)
       
#turtle.speed('fastest')

turtle.penup()
turtle.goto(-250, 0)
turtle.pendown()

kantorov(500, 5, -250, 0)