#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 20 17:49:46 2020

@author: vladislav

SOLAR SYSTEM
"""

import graphics as gr

SIZE_X = 400
SIZE_Y = 400
BALL_RADIUS = 10

window = gr.GraphWin("SOLAR SYSTEM", SIZE_X, SIZE_Y)

# Initial position of ball
coords = gr.Point(SIZE_X / 2, SIZE_Y / 2)

# Velocity
velocity = gr.Point(2, 2)

# Acceleration
acceleration = gr.Point(0, 1)

def add(point_1, point_2):
    """
    Calculates next position of point

    Parameters
    ----------
    point_1 : Tuple of Int
        Actual position of point.
    point_2 : Tuple of Int
        Velocity of point.

    Returns
    -------
    new_point : Tuple of Int
        New point.

    """
    new_point = gr.Point(point_1.x + point_2.x,
                      point_1.y + point_2.y)
    return new_point

def draw_circle(coords):
    """
    Draws a Ball

    Parameters
    ----------
    coords : Tuple of Int
        Coordinates of the ball center.

    Returns
    -------
    Draws a new ball.

    """
    circle = gr.Circle(coords, BALL_RADIUS)
    circle.setFill('red')
    
    circle.draw(window)
    
def clear_window():
    """
    Clears window

    Returns
    -------
    None.

    """
    rectangle = gr.Rectangle(gr.Point(0, 0), 
                             gr.Point(SIZE_X, SIZE_Y))
    rectangle.setFill('gray')
    rectangle.draw(window)
    
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
    if 0 > coords.y - BALL_RADIUS  or coords.y + BALL_RADIUS > SIZE_Y:
        velocity.y = -velocity.y
        
    if 0 > coords.x - BALL_RADIUS or coords.x + BALL_RADIUS > SIZE_X:
        velocity.x = -velocity.x
    
def update_velocity(velocity, acceleration):
    """
    Update velocity using gravity

    Parameters
    ----------
    velocity : Tuple of int
        Ball velocity
    acceleration : Tuple of int
        Ball gravity.

    Returns
    -------
    None.

    """    
    return add(velocity, acceleration)
while True:
    clear_window()
    
    draw_circle(coords)
    coords = add(coords, velocity)
    velocity = update_velocity(velocity, acceleration)
    check_coords(coords, velocity)
    
    gr.time.sleep(0.02)

window.getMouse()

window.close()
