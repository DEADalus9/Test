#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_6_6():
    
    
    
    state = 0
    
    while True:
        
        if state == 0:
            move_right()
            if not wall_is_above():
                state = 10
            if wall_is_on_the_right() and wall_is_beneath() and wall_is_above():
                state = 30
        elif state == 10:
            move_up()
            fill_cell()
            if wall_is_above():
                state = 20
        elif state == 20:
            move_down()
            if wall_is_beneath():
                state = 0
            if wall_is_beneath() and wall_is_on_the_right() and not wall_is_above():
                state = 30
        elif state == 30:
            move_left()
            if not wall_is_beneath():
                break
         
        


if __name__ == '__main__':
    run_tasks()
