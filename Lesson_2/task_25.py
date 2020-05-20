#!/usr/bin/python3

from pyrob.api import *

def cross():
    for i in range(2):
        move_down()
    fill_cell()
    for i in range(2):
        move_right()
        fill_cell()
    move_left()
    move_down()
    move_down()
    for i in range(3):
        move_up()
        fill_cell()
    move_left()
    
def go_to():
    move_up()
    move_right(n = 4)    

@task
def task_2_2():
    
    for i in range(4):
        cross()
        go_to()
    cross()

if __name__ == '__main__':
    run_tasks()
