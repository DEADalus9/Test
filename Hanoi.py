#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 19 18:07:31 2020

@author: vladislav

Hanoi towers

"""

import tkinter as tk 


class Rod():
    
    def __init__(self):
        pass
    
    def draw():
        pass

    
class Disc():

    def __init__(self):
        pass
    
    def draw():
        pass
    

def window_init():
    
    window = tk.Tk()
    window.title('HANOI TOWERS')
    window.geometry('800x600')
    window.mainloop()
    
    
def hanoi(n, rod_1, rod_2, rod_3):
    """
    
    Parameters
    ----------
    n : amount of discs.

    Returns
    -------
    count changes

    """
    if n == 1:
        print ('Take disc {} from {} to {}'.format(n, rod_1, rod_2))
        return
    hanoi(n - 1, rod_1, rod_3, rod_2)
    print ('Take disc {} from {} to {}'.format(n, rod_1, rod_2))  
    hanoi(n - 1, rod_3, rod_2, rod_1)  

def main():
    """
    main function to realize algorythm

    Returns
    -------
    None.

    """
    
#    n = 3
#    hanoi(n, 1, 2, 3)
    
    window_init()


if __name__ == '__main__':
    main()