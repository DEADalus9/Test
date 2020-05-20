#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 20 17:04:27 2020

@author: vladislav

HOUSE WITH STRUCTURE AND PARAMETERS
"""

import graphics as gr

# GRAPHICS INIT

window = gr.GraphWin('PAINTURE WITH STRUCTURE', 800, 600)

# SKY
def sky():
    """
    Draws sky - fills area with Light Blue color

    Returns
    -------
    None.

    """
    sky = gr.Rectangle(gr.Point(0, 0), gr.Point(800, 400))
    sky.setFill('LightBlue')
    sky.setOutline('LightBlue')
    sky.draw(window)

# EARTH
def earth():
    """
    Draws earth - fills area with Light Gray color

    Returns
    -------
    None.

    """
    earth = gr.Rectangle(gr.Point(0, 400), 
                         gr.Point(800, 600))
    earth.setFill(gr.color_rgb(187, 187, 187))
    earth.setOutline(gr.color_rgb(187, 187, 187))
    earth.draw(window)

# CLOUDS
def cloud(x, y, scale):
    """
    Draws cloud in window

    Parameters
    ----------
    x : INT
        Horizontal position.
    y : INT
        Vertical position.
    scale : FLOAT
        Scale factor.

    Returns
    -------
    SHOWING CLOUD.

    """
    
    shift_x = 0
    shift_y = 0
    k = 1
    for i in range(2):
        for j in range(3 - k):
            cloud = gr.Circle(gr.Point(x + shift_x, 
                                       y + shift_y), 
                                         30 * scale)
            cloud.setFill('White')
            cloud.draw(window)
            shift_x += 20 * scale
        shift_x = -30 * scale / 2
        shift_y += 20 * scale
        k -= 1

# TREE
def tree(x, y):
    """
    Draws tree in windows

    Parameters
    ----------
    x : INT
        Horizontal position - middle of rod.
    y : INT
        Vertical position - lower position of rod.

    Returns
    -------
    None.

    """
    tree_rod = gr.Rectangle(gr.Point(x - 10, y - 50),
                            gr.Point(x + 10, y))
    tree_rod.setFill('Brown')
    tree_rod.draw(window)
    
    for i in range(3):
        tree = gr.Polygon(gr.Point(x - 100 + 25 * i, y - 50 - 50 * i), 
                          gr.Point(x               , y - 50 - 60 - 50 * i), 
                          gr.Point(x + 100 - 25 * i, y - 50 - 50 * i))
        tree.setFill('Green')
        tree.draw(window)

# HOUSE
def house(x, y):
    """
    Draws house

    Parameters
    ----------
    x : INT
        Horizontal position of left bottom corner.
    y : INT
        Vertical position of left bottom corner.

    Returns
    -------
    None.

    """
    house_body = gr.Rectangle(gr.Point(x, y - 200),
                              gr.Point(x + 200, y))
    house_body.setFill('Gray')
    house_body.draw(window)
    
    house_chimney = gr.Rectangle(gr.Point(x + 140, y - 280), 
                                 gr.Point(x + 160, y - 200))
    house_chimney.setFill('Gray')
    house_chimney.draw(window)
    
    house_roof = gr.Polygon(gr.Point(x      , y - 200),
                            gr.Point(x + 100, y - 300),
                            gr.Point(x + 200, y - 200))
    house_roof.setFill('Maroon')
    house_roof.draw(window)
    
    house_roof_window = gr.Circle(gr.Point(x + 100, y - 235), 
                                  15)
    house_roof_window.setFill(gr.color_rgb(255,251,130))
    house_roof_window.draw(window)
    
    for i in range(2):
        for j in range(2):
            house_body_window = gr.Rectangle(gr.Point(x + 70 + 30 * j , y - 130 + 30 * i),
                                             gr.Point(x + 100 + 30 * j, y - 100 + 30 * i))
            house_body_window.setFill('Yellow')
            house_body_window.setWidth(3)
            house_body_window.draw(window)

# SUN
def sun(x, y, R):
    """
    Draws sun

    Parameters
    ----------
    x : INT
        Horizontal position.
    y : INT
        Vertical position.
    R : INT
        Radius of sun

    Returns
    -------
    None.

    """
    sun = gr.Circle(gr.Point(x, y), R)
    sun.setFill('Yellow')
    sun.setOutline('Yellow')
    sun.draw(window)

# DRAW
def draw_painture():
    sky()
    earth()
    cloud(100, 170, 1.1)
    cloud(400, 100, 0.7)
    cloud(600, 180, 0.2)
    cloud(520, 50, 0.1)
    house(350, 450)
    tree(200, 470)
    tree(250, 500)
    tree(600, 430)
    sun(700, 100, 30)
    

draw_painture()

window.getMouse()

window.close()