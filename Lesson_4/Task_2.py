#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 20 19:14:01 2020

@author: vladislav

MATHEMATICAL PENDULUM
"""

import graphics as gr
import math

G = 0.1
SIZE_X = 400
SIZE_Y = 400
BALL_RADIUS = 10


window = gr.GraphWin('MATHEMATICAL PENDULUM', SIZE_X, SIZE_Y)

# Initial point of pendulum
coords = gr.Point(100, 200)

# Previous point of pendulum
coords_old = gr.Point(100, 200)

# Zero point
zero_coords = gr.Point(SIZE_X / 2, 0)

# Initial velocity of pendulum
velocity = gr.Point(0, 0)

# Initial acceleration
acceleration = gr.Point(0, 0)

def sub(point_1, point_2):
    return gr.Point(point_1.x - point_2.x,
                    point_1.y - point_2.y)

def add(point_1, point_2):
    return gr.Point(point_1.x + point_2.x,
                    point_1.y + point_2.y)

def update_velocity(velocity, acceleration):
    return add(velocity, acceleration)

def update_coords(coords, velocity):
    return add(coords, velocity)

length = ((sub(coords, zero_coords).x) ** 2 + 
          (sub(coords, zero_coords).y) ** 2) ** 0.5

print(length)

def check_coordinates(coords, zero_coords):
    """    
    distance = sub(coords, zero_coords)
    distance_2 = (distance.x ** 2 + distance.y ** 2) ** 0.5
    print('distance =', distance_2)
    coords = gr.Point(coords.x + distance_2 + length, 
                      coords.y + distance_2 + length)
    """    
    if coords.x == SIZE_X / 2:
        coords.y = length
    elif coords.x < SIZE_X / 2:
        coords.y = length
    else:
        coords.y = length

    

def check_coords(coords, velocity):
    """
    Check colission between Ball and Walls

    Parameters
    ----------
    coords : Tuple of Int
        Coordinates of Ball.
    velocity : Int
        Velocity of Ball.

    Returns
    -------
    None.

    """
    if 0 >= coords.y - BALL_RADIUS  or coords.y + BALL_RADIUS >= SIZE_Y:
        velocity.y = -velocity.y
        
    if 0 >= coords.x - BALL_RADIUS or coords.x + BALL_RADIUS >= SIZE_X:
        velocity.x = -velocity.x    

def update_acceleration(ball_coords, center_coords):
    accel_x = (ball_coords.x / length) ** 2 * G
    accel_y = length - ball_coords.y
    print('acc_x = {} acc_y = {}'.format(accel_x, accel_y))
    if ball_coords.x < SIZE_X / 2:
        return gr.Point(accel_x, -accel_y)
    elif ball_coords.x == 0:
        return gr.Point(0, 0)
    else:
        return gr.Point(-accel_x , accel_y)

ball = gr.Circle(coords, BALL_RADIUS)
ball.setFill('blue')
ball.draw(window)

def cord_line(cords, zero_cords):
    cord = gr.Line(coords, zero_coords)
    cord.setWidth(3)
    cord.draw(window)

while True:
    
    acceleration = update_acceleration(coords, zero_coords)
    
    velocity = update_velocity(velocity, acceleration)
    
    coords = update_coords(coords, velocity)
    
    #check_coordinates(coords, zero_coords)
    
    check_coords(coords, velocity)
    
    deltas = sub(coords, coords_old)
    ball.move(deltas.x, deltas.y)
    
    #cord_line(coords, zero_coords)
    coords_old = gr.Point(coords.x, coords.y)