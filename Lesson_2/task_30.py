#!/usr/bin/python3

from pyrob.api import *


#def stepper(size):
#    row = 0
#    column = 0
    
#    while not wall_is_on_the_left():
        
    


def draw_cycle(side_length):
    i = 0
    while i < side_length - 1:
        if i > 0:
            fill_cell()
            move_up()
        else:
            move_up()
        i += 1
    i = 0
    while i < side_length - 1:
        if i > 0:
            fill_cell()
            move_right()
        else:
            move_right()
        i += 1
    i = 0
    while i < side_length - 1:
        if i > 0:
            fill_cell()
            move_down()
        else:
            move_down()
        i += 1
    i = 0
    while i < side_length - 1:
        if i > 0:
            fill_cell()
            move_left()
        else:
            move_left()
        i += 1

    

@task(delay=0.5)
def task_9_3():
    
    """
        size = 0
         
        while not wall_is_on_the_right():
            size += 1
            move_right()
        
        stepper()
    """    

    side_length = 1
    while not wall_is_beneath():
        move_down()
        side_length += 1
    while side_length > 1:
        draw_cycle(side_length)
        move_right()
        move_up()
        side_length -= 2
    while not wall_is_beneath():
        move_down()
    while not wall_is_on_the_left():
        move_left()  
    

if __name__ == '__main__':
    run_tasks()
