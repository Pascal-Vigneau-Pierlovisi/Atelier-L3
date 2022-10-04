# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#  Pascal Vigneau Pierlovisi, le 4 Octobre 2022

import numpy as np
objects = np.loadtxt('Sac_a_dos.txt', dtype=int)
print(objects)
W=15
n=len(objects)
C=[0]*W
Cnext = [0]*W


for i in range(n):
    for w in range(W):
        if (w >=objects[i][2]):
            Cnext[w] = max(C[w], C[w-objects[i][2]] + objects[i][1])
        else:
            Cnext[w] = C[w]
    print(Cnext)
    C = Cnext.copy()