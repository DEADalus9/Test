#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 21 22:52:27 2020

@author: vladislav
"""

import graphics as gr

SIZE_X = 400
SIZE_Y = 400
BALL_RADIUS = 10
G = 35000


window = gr.GraphWin('MATHEMATICAL PENDULUM', SIZE_X, SIZE_Y)

coords = gr.Point(50, 150)

zero_coords = gr.Point(SIZE_X // 2, 0)

coords_old = gr.Point(50, 150)

velocity = gr.Point(0.0, 0.0)

acceleration = gr.Point(0, 10)

def sub(point_1, point_2):
    return gr.Point(point_1.x - point_2.x,
                    point_1.y - point_2.y)

def distance(point_1, point_2):
    delta = sub(point_1, point_2)
    return (delta.x ** 2 + delta.y ** 2) ** 0.5

r = distance(zero_coords, coords) 

def add(point_1, point_2):
    return gr.Point(point_1.x + point_2.x,
                    point_1.y + point_2.y)

def update_coords(coords, velocity):
    return add(coords, velocity)

def update_velocity(velocity, acceleration):
    return add(velocity, acceleration)

def update_acceleration(coords):
    delta = sub(zero_coords, coords)
    return gr.Point(G * delta.x / r ** 3, G * delta.y / r ** 3)

def check_coords(coords, velocity):
    if 0 >= coords.y - BALL_RADIUS  or coords.y + BALL_RADIUS >= SIZE_Y:
        velocity.y = -velocity.y
        
    if 0 >= coords.x - BALL_RADIUS or coords.x + BALL_RADIUS >= SIZE_X:
        velocity.x = -velocity.x

def cord_line(cords, zero_cords):
    cord = gr.Line(coords, zero_coords)
    cord.setWidth(3)
    cord.draw(window)

ball = gr.Circle(coords, BALL_RADIUS)
ball.setFill('green')
ball.draw(window)

while True:
    
    velocity = update_velocity(velocity, acceleration)
    
    coords = update_coords(coords, velocity)
    
    acceleration = update_acceleration(coords)
    
    #check_coords(coords, velocity)
    
    deltas = sub(coords, coords_old)
   
    ball.move(deltas.x, deltas.y)
    
    cord_line(coords, zero_coords)
    
    coords_old = gr.Point(coords.x, coords.y)
    
    gr.time.sleep(0.02)