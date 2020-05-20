#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed May 20 14:39:31 2020

@author: vladislav

HOUSE WITHOUT STRUCTURE
"""

import graphics as gr

# GRAPHICS INIT

window = gr.GraphWin('PAINTURE', 800, 600)

# SKY
sky = gr.Rectangle(gr.Point(0, 0), gr.Point(800, 400))
sky.setFill('LightBlue')
sky.setOutline('LightBlue')
sky.draw(window)

# EARTH
earth = gr.Rectangle(gr.Point(0, 400), 
                     gr.Point(800, 600))
earth.setFill(gr.color_rgb(187, 187, 187))
earth.setOutline(gr.color_rgb(187, 187, 187))
earth.draw(window)

# CLOUD
shift = 0
k = 0
for i in range(2):
    for j in range(3 - k):
        cloud = gr.Circle(gr.Point(100 + 20 * j + shift, 170 - 20 * i), 30)
        cloud.setFill('White')
        cloud.draw(window)
    shift += 10
    k += 1

# TREE
tree_rod = gr.Rectangle(gr.Point(590, 420),
                        gr.Point(610, 470))
tree_rod.setFill('Brown')
tree_rod.draw(window)

for i in range(3):
    tree = gr.Polygon(gr.Point(500 + 25 * i, 420 - 50 * i), 
                      gr.Point(600         , 360 - 50 * i), 
                      gr.Point(700 - 25 * i, 420 - 50 * i))
    tree.setFill('Green')
    tree.draw(window)

# HOUSE
house_body = gr.Rectangle(gr.Point(250, 250),
                          gr.Point(450, 450))
house_body.setFill('Gray')
house_body.draw(window)

house_chimney = gr.Rectangle(gr.Point(390, 170), 
                             gr.Point(410, 250))
house_chimney.setFill('Gray')
house_chimney.draw(window)

house_roof = gr.Polygon(gr.Point(250, 250),
                        gr.Point(350, 150),
                        gr.Point(450, 250))
house_roof.setFill('Maroon')
house_roof.draw(window)

house_roof_window = gr.Circle(gr.Point(350, 215), 
                              15)
house_roof_window.setFill(gr.color_rgb(255,251,130))
house_roof_window.draw(window)

for i in range(2):
    for j in range(2):
        house_body_window = gr.Rectangle(gr.Point(320 + 30 * j, 320 + 30 * i),
                                         gr.Point(350 + 30 * j, 350 + 30 * i))
        house_body_window.setFill('Yellow')
        house_body_window.setWidth(3)
        house_body_window.draw(window)

# SUN
sun = gr.Circle(gr.Point(700, 100), 50)
sun.setFill('Yellow')
sun.setOutline('Yellow')
sun.draw(window)

# DRAW

#house.draw(window)

window.getMouse()

window.close()