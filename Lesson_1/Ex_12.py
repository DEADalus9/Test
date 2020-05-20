#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 12 19:28:05 2020

@author: vladislav
"""

import turtle


def circle_left(n):
    for i in range(180):
        turtle.forward(n)
        turtle.left(1)
        
def circle_right(n):
    for i in range(180):
        turtle.forward(n)
        turtle.right(1)


def spring(m):
    for i in range(m):
        circle_right(0.5)
        circle_right(0.1)
 
   
turtle.shape('turtle')
turtle.left(90)
spring(5)