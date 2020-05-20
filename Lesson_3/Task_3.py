#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 20 16:44:12 2020

@author: vladislav

HOUSE WITH STRUCTURE
"""

import graphics as gr

# GRAPHICS INIT

window = gr.GraphWin('PAINTURE WITH STRUCTURE', 800, 600)

# SKY
def sky():
    sky = gr.Rectangle(gr.Point(0, 0), gr.Point(800, 400))
    sky.setFill('LightBlue')
    sky.setOutline('LightBlue')
    sky.draw(window)

# EARTH
def earth():
    earth = gr.Rectangle(gr.Point(0, 400), 
                         gr.Point(800, 600))
    earth.setFill(gr.color_rgb(187, 187, 187))
    earth.setOutline(gr.color_rgb(187, 187, 187))
    earth.draw(window)

# CLOUDS
def cloud_1():
    shift = 0
    k = 0
    for i in range(2):
        for j in range(3 - k):
            cloud = gr.Circle(gr.Point(100 + 20 * j + shift, 170 - 20 * i), 30)
            cloud.setFill('White')
            cloud.draw(window)
        shift += 10
        k += 1

def cloud_2():
    shift = 0
    k = 0
    for i in range(2):
        for j in range(3 - k):
            cloud = gr.Circle(gr.Point(400 + 20 * j + shift, 100 - 20 * i), 30)
            cloud.setFill('White')
            cloud.draw(window)
        shift += 10
        k += 1

def cloud_3():
    shift = 0
    k = 0
    for i in range(2):
        for j in range(3 - k):
            cloud = gr.Circle(gr.Point(600 + 20 * j + shift, 180 - 20 * i), 30)
            cloud.setFill('White')
            cloud.draw(window)
        shift += 10
        k += 1

# TREE
def tree():
    tree_rod = gr.Rectangle(gr.Point(190, 420),
                            gr.Point(210, 470))
    tree_rod.setFill('Brown')
    tree_rod.draw(window)
    
    for i in range(3):
        tree = gr.Polygon(gr.Point(100 + 25 * i, 420 - 50 * i), 
                          gr.Point(200         , 360 - 50 * i), 
                          gr.Point(300 - 25 * i, 420 - 50 * i))
        tree.setFill('Green')
        tree.draw(window)

# HOUSE
def house():
    house_body = gr.Rectangle(gr.Point(450, 250),
                              gr.Point(650, 450))
    house_body.setFill('Gray')
    house_body.draw(window)
    
    house_chimney = gr.Rectangle(gr.Point(590, 170), 
                                 gr.Point(610, 250))
    house_chimney.setFill('Gray')
    house_chimney.draw(window)
    
    house_roof = gr.Polygon(gr.Point(450, 250),
                            gr.Point(550, 150),
                            gr.Point(650, 250))
    house_roof.setFill('Maroon')
    house_roof.draw(window)
    
    house_roof_window = gr.Circle(gr.Point(550, 215), 
                                  15)
    house_roof_window.setFill(gr.color_rgb(255,251,130))
    house_roof_window.draw(window)
    
    for i in range(2):
        for j in range(2):
            house_body_window = gr.Rectangle(gr.Point(520 + 30 * j, 320 + 30 * i),
                                             gr.Point(550 + 30 * j, 350 + 30 * i))
            house_body_window.setFill('Yellow')
            house_body_window.setWidth(3)
            house_body_window.draw(window)

# SUN
def sun():
    sun = gr.Circle(gr.Point(700, 100), 50)
    sun.setFill('Yellow')
    sun.setOutline('Yellow')
    sun.draw(window)

# DRAW
def draw_painture():
    sky()
    earth()
    cloud_1()
    cloud_2()
    cloud_3()
    tree()
    house()
    sun()
    

draw_painture()

window.getMouse()

window.close()