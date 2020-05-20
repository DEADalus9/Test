#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_29():
        
    state = 0
    while True:
        
        if state == 0:
            move_left()
            if wall_is_on_the_left():
                state = 10
        elif state == 10:
            if not wall_is_above():
                state = 40
                continue
            move_right()
            if wall_is_on_the_right():
                state = 20
        elif state == 20:
            if wall_is_above() and wall_is_beneath():
                break
            move_up()
            if wall_is_above():
                state = 30
        elif state == 30:
            move_left()
            if wall_is_on_the_left():
                break
        elif state == 40:
            move_up()
            if wall_is_above():
                break
        else:
            break
        
       
        

    

if __name__ == '__main__':
    run_tasks()
