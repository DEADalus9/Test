#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 12 19:28:05 2020

@author: vladislav
"""

import turtle


def circle_left(n, clr):
    turtle.color('black')
    turtle.begin_fill()
    for i in range(360):
        turtle.forward(n)
        turtle.left(1)
    turtle.color(clr)      
    turtle.forward(n)
    turtle.left(1)        
    turtle.end_fill()
    
    
    #turtle.color('black')
        
def circle_right(n, clr):
    turtle.color(clr)
    for i in range(180):
        turtle.forward(n)
        turtle.right(1)

def draw_line(n, clr, width):
    turtle.right(90)
    turtle.color(clr)
    turtle.width(width)
    turtle.forward(n)
    turtle.width()
    turtle.color()

def move_to(x, y):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()


def face():
    move_to(0, -100)
    circle_left(3, 'yellow')
    move_to(-80, 120)
    circle_left(0.3, 'blue')
    move_to(80, 120)
    circle_left(0.3, 'blue')
    move_to(0, 100)
    draw_line(70, 'black', 10)
    move_to(60, -10)
    circle_right(1, 'red')
    
 
   
turtle.shape('turtle')
turtle.speed('fastest')
face()