#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 12 19:28:05 2020

@author: vladislav
"""

import turtle

def spider(n, length):
    angle_step = 360 / n
    for i in range(n):
        turtle.left(i * angle_step)
        print(i * angle_step)
        turtle.forward(length)
        turtle.stamp()
        turtle.left(180)
        turtle.forward(length)
        turtle.left(180 - i * angle_step)


turtle.shape('turtle')

spider(24, 100)