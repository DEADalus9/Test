#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 12 19:28:05 2020

@author: vladislav
"""

import turtle
import math

def figure(m, length):
    """
    Fuction to draw figure with n shapes 

    Parameters
    ----------
    n : Number of shapes.

    Returns
    -------
    Shape.

    """
    turtle.penup()
    turtle.goto(23, 0)
    turtle.pendown()
    
    for j in range(3, m + 3):
        angle = 360 / j
        turtle.left((180 - angle) / 2)
        for i in range(j):
            turtle.left(angle)
            turtle.forward(2 * (j * 10) * math.sin(360 * math.pi / 180 / 2 / j))
        turtle.penup()
        turtle.goto(j * 10, 0)
        turtle.pendown()
        turtle.right((180 - angle) / 2)
   
turtle.shape('turtle')
figure(30, 100)

