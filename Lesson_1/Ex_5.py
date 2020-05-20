#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 12 19:28:05 2020

@author: vladislav
"""

def square(length):
    for i in range(4):
        turtle.forward(length)
        turtle.left(90)

import turtle

turtle.shape('turtle')

for i in range(1,10):
    turtle.penup()
    turtle.goto(-5 * i, -5 * i)
    turtle.pendown()
    square(10 * i)