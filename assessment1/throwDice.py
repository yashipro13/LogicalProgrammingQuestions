# -*- coding: utf-8 -*-
"""
Created on Fri Jun  7 18:33:29 2019

@author: yashi
"""

import random
def throwDice(times):
    count = [0]*6
    for i in range (times):
        num_on_top1 = random.randint(1,6)
        count[num_on_top1-1] = count[num_on_top1-1] + 1
    return count

print(throwDice(10000))
expectedThrows = [round(10000/6,0)]*6
print(expectedThrows) 