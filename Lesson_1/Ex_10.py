#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 12 19:28:05 2020

@author: vladislav
"""

import turtle


def circle_left():
    for i in range(360):
        turtle.forward(1)
        turtle.left(1)
        
def circle_right():
    for i in range(360):
        turtle.forward(1)
        turtle.right(1)


def flower():
    for i in range(3):
        circle_left()
        circle_right()
        turtle.left(120)
   
turtle.shape('turtle')
flower()