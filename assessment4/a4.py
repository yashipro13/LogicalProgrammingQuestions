# -*- coding: utf-8 -*-
"""
Created on Fri Jun 14 16:24:23 2019

@author: yashi
"""

def separateStepDirection(step_string):
    i = 0
    while step_string[i] >= '0' and step_string[i] <= '9':
        i = i + 1
    return int(step_string[ : i]) , step_string[i:]

def nextPartialStep(direction, newPos, step):
    if direction == 'N':
        newPos[1] += step
    elif direction == 'S':
        newPos[1] -= step
    elif direction == 'E':
        newPos[0] += step
    elif direction == 'W':
        newPos[0] -= step
    return newPos

def newPosition (oldPos, step, direction):
    i = 0
    newPos = oldPos
    while i < len(direction):
        newPos = nextPartialStep(direction[i], newPos, step)
        i = i + 1
    return newPos

def terminus (lattice_point, directions):
    curr_pos = list(lattice_point)
    for each in directions:
        step , direction = separateStepDirection (each)
        curr_pos = newPosition(curr_pos, step, direction)
    return tuple(curr_pos)

print(terminus((-1, 1), ["1NE"]))




