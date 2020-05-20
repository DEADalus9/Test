#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_7():
    position = 0
    
    while not wall_is_on_the_right():
        move_right()
        if cell_is_filled():
            position += 1
        else:
            position = 0
        
        if position >= 3:
            break


if __name__ == '__main__':
    run_tasks()
