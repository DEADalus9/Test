#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 20 13:39:55 2020

@author: vladislav

CRAZY FACE
"""


from graph import *

# FACE
penColor(0, 0, 0)
penSize(2)
brushColor('yellow')
circle(250, 250, 200)

# RIGHT EYE
brushColor('red')
circle(150, 190, 40)
brushColor('black')
circle(150, 190, 10)
penSize(20)
line(200, 165, 50, 50)
penSize(2)

# LEFT EYE
brushColor('red')
circle(350, 190, 30)
brushColor('black')
circle(350, 190, 10)
penSize(20)
line(300, 165, 470, 100)
penSize(2)

# MOUTH
brushColor('black')
rectangle(150, 320, 350, 370)

run()