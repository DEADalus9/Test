#!/usr/bin/python3

from pyrob.api import *

def cross():
    for i in range(2):
        move_down()
    for i in range(3):
        move_right()
        fill_cell()
    move_left()
    move_down()
    move_down()
    for i in range(3):
        move_up()
        fill_cell()
    move_left()

@task
def task_2_1():
    cross()


if __name__ == '__main__':
    run_tasks()
