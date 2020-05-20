#!/usr/bin/python3

from pyrob.api import *

def cross():
    move_down()
    fill_cell()
    for i in range(2):
        move_right()
        fill_cell()
    move_left()
    move_down()
    fill_cell() 
    for i in range(2):
        move_up()
        fill_cell()
    move_left()
    
def go_to_x(direction, points):
    if direction == 'right':
        move_right(points)
    else:
        move_left(points)

def go_to_y():
    move_down(n = 4)
    
def line(direction):
    for i in range(9):
        cross()
        go_to_x(direction, 4)
    cross()
    


@task(delay=0.02)
def task_2_4():
    for j in range(2):
        line('right')
        go_to_y()
        line('left')
        go_to_y()
    line('right')
    go_to_x('left', 36)

if __name__ == '__main__':
    run_tasks()
