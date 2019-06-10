# -*- coding: utf-8 -*-
"""
Created on Mon Jun 10 16:37:08 2019

@author: yashi
"""
def playRps (c1, c2):
    if c1 == c2:
        return 0
    elif (c1 == 'R' and c2 == 'P') or (c1 == 'S' and c2 == 'R' ) and (c1 == 'P' and c2 == 'R'):
        return -1
    else:
        return 1

def rps(input_string):
    gameList = list(input_string.split(','))
    result = {'+':0, '-':0, '=':0,}
    for each in gameList:
        if playRps(each[0], each[1]) == 0:
            result['='] += 1
        elif playRps(each[0], each[1]) == 1:
            result['+'] += 1
        else:
            result['-'] += 1
    return result
print(rps("RR,RP,RS,SS,SR"))