#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_10():
    
    state = 0
    fill_cell()
    while True:
        if state == 0 and not wall_is_on_the_right():
            move_right()
            fill_cell()
            if wall_is_on_the_right() and not wall_is_beneath():
                move_down()
                fill_cell()
                state = 10
            elif wall_is_on_the_right() and wall_is_beneath():
                state = 10
        elif state == 10 and not wall_is_on_the_left():
            move_left()
            fill_cell()
            if wall_is_on_the_left() and not wall_is_beneath():
                move_down()
                fill_cell()
                state = 0
            elif wall_is_on_the_left() and wall_is_beneath():
                break
        else:
            break
         

        

if __name__ == '__main__':
    run_tasks()
