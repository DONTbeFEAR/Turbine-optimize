# -*- coding: utf-8 -*-
"""
Created on Fri Oct 03 21:39:17 2014

@author: Eric
"""
import numpy as np
from CurvePoints import CurvePoints

def CS(fileP,fileCS):
    P = np.genfromtxt(fileP)
    U = np.genfromtxt('knot_vector.dat')
    p = 3
    numofpoints = 31
    CS = CurvePoints(numofpoints,p,U,P)
    np.savetxt(fileCS,CS,fmt='%.8f')
    return True

if __name__ == '__main__':
    pass