#!/usr/bin/python3

from pyrob.api import *



@task
def task_7_6():
    position = 0
    while True:
        move_right()
        if cell_is_filled():
            position += 1
        
        if position >= 5:
            break
    
    


if __name__ == '__main__':
    run_tasks()
