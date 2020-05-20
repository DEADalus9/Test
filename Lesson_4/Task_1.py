#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 20 17:49:46 2020

@author: vladislav

SOLAR SYSTEM
"""

import graphics as gr

SIZE_X = 800
SIZE_Y = 800
BALL_RADIUS = 10
G = 2000

window = gr.GraphWin("SOLAR SYSTEM", SIZE_X, SIZE_Y)

# Initial position of ball
coords = gr.Point(400, 700)

old_coords = gr.Point(400, 700)

# Velocity
velocity = gr.Point(2, 0)

# Acceleration
acceleration = gr.Point(0, 0)

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

def sub(point_1, point_2):
    """
    Calculation of new coordinate before point

    Parameters
    ----------
    point_1 : Tuple of Int
        Coordinates of old point.
    point_2 : Tuple of int
        Coordinates of velocities.

    Returns
    -------
    None.

    """
    new_point = gr.Point(point_1.x - point_2.x,
                         point_1.y - point_2.y)
    
    return new_point 

def draw_ball(coords):
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
    if 0 >= coords.y - BALL_RADIUS  or coords.y + BALL_RADIUS >= SIZE_Y:
        velocity.y = -velocity.y
        
    if 0 >= coords.x - BALL_RADIUS or coords.x + BALL_RADIUS >= SIZE_X:
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

def update_coordinates(coords, velocity):
    return add(coords, velocity)

def update_acceleration(ball_coords, center_coords):
    diff = sub(ball_coords, center_coords)
    distance_2 = (diff.x ** 2 + diff.y ** 2) ** (3 / 2)
    return gr.Point(-diff.x * G / distance_2, -diff.y * G / distance_2) 

circle = gr.Circle(coords, BALL_RADIUS)
circle.setFill('red')
circle.draw(window)

sun = gr.Circle(gr.Point(400, 400), 50)
sun.setFill('yellow')
sun.draw(window)

while True:
    
    
    
    #clear_window()
    
    acceleration = update_acceleration(coords, gr.Point(400, 400))
    
    coords = update_coordinates(coords, velocity)
    
    velocity = update_velocity(velocity, acceleration)
    
    check_coords(coords, velocity)
    
    deltas = sub(coords, old_coords)
    circle.move(deltas.x, deltas.y)
    
    old_coords = gr.Point(coords.x, coords.y)
    
    gr.time.sleep(0.02)
