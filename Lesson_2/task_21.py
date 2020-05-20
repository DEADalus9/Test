#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():
    move_right()
    move_down()
    fill_cell()
    move_down()
    
    for i in range(2, 14):
        fill_cell()
        for j in range(1, i):
            move_right()
            fill_cell()

        for j in range(1, i):
            move_left()

        move_down()
        
if __name__ == '__main__':
    run_tasks()
