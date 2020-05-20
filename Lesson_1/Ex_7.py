#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 12 19:28:05 2020

@author: vladislav
"""

import turtle

def round_helix(n):
    for i in range(n):
        turtle.forward(i / n)
        turtle.left(1)

turtle.shape('turtle')
turtle.speed('fastest')

round_helix(5000)