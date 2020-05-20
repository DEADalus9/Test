#!/usr/bin/python3

from pyrob.api import *


def move_up_line():
    val = 0
    while not wall_is_above():
        move_up()
        if cell_is_filled():
            val += 1
        else:
            fill_cell()
            
    while not wall_is_beneath():
        move_down()
    
    return val
        
def move_right_line():
    if wall_is_above():
        fill_cell()
    move_right()        

@task(delay=0.05)
def task_8_18():
   
    ax = 0
    
    while not wall_is_on_the_right():
        move_right_line()
        if wall_is_beneath():
          ax += move_up_line()
    mov('ax', ax)
    print(ax)
    
    


if __name__ == '__main__':
    run_tasks()
