#!/usr/bin/python3

from pyrob.api import *

def line():
    state = 0
    count = 0
    
    while True: 
        if state == 0 and count != 2:
            move_left()
            if wall_is_on_the_left():
                state = 10
                count += 1
            
        elif state == 10 and count != 2:
            move_right()
            if wall_is_on_the_right():
                state = 0
                count += 1
            
        if not wall_is_beneath():
            move_down()
            count = 0
        
        if count == 2:
            if wall_is_on_the_left():
                break
            move_left()
        


@task(delay=0.01)
def task_8_30():
    line()


if __name__ == '__main__':
    run_tasks()
