#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 12 19:28:05 2020

@author: vladislav
"""

import turtle



def star(n):
    turtle.penup()
    turtle.goto(100, 50)
    turtle.pendown()
    alpha = 180 / n    
    for i in range(n):
        turtle.left(180 - alpha)
        turtle.forward(200)
        
   
turtle.shape('turtle')
turtle.speed('fastest')
star(21)