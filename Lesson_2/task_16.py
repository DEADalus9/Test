#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_22():
    pos = False
    turned = False
    while True:
        if wall_is_on_the_left() and wall_is_on_the_right():
            move_up()
        elif wall_is_on_the_left() and not wall_is_on_the_right() and not turned:
            move_right()
            pos = True
            turned = True
        elif not wall_is_on_the_left() and wall_is_on_the_right() and not turned:
            move_left()
            turned = True
        elif wall_is_above() and wall_is_beneath():
            if pos:
                if wall_is_on_the_right():
                    break
                move_right()
             
            else:
                if wall_is_on_the_left():
                    break
                move_left()
                

if __name__ == '__main__':
    run_tasks()
