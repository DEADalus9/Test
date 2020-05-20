#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_28():
    left_reached = False
    
    while True:
        if not(wall_is_on_the_left()) and not left_reached:
            move_left()
        else:
            left_reached = True
            move_right()
        if not wall_is_above() or not wall_is_beneath():
            break
        
    while True:
        if not wall_is_above():
            move_up()
        elif not wall_is_on_the_left():
            move_left()
        else:
            break
        left_reached = False
        


if __name__ == '__main__':
    run_tasks()
