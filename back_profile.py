# -*- coding: utf-8 -*-
"""
Created on Fri Oct 03 10:14:12 2014

@author: Eric
"""

import numpy as np
from PyNURBS import CurvePoints

def back_profile(filename1,filename2):
    #指定插值曲线次数
    p = 3
    #求得控制点
    P = np.genfromtxt(filename1)
    #求解插值后曲线上更多的点
    U = np.genfromtxt('KnotVector.dat')
    numofpoints = 31
    Cs = CurvePoints.CurvePoints(numofpoints,p,U,P).tolist()
    Css = [[0.0000,0.00000,-35.000],
           [0.0000,0.00000,-60.000],
           [0.0000,100.000,-60.000],
           [0.0000,100.000,20.0000],
           [0.0000,87.4763,20.0000],
           [0.0000,87.4763,-1.0000]]

    np.savetxt(filename2,Cs+Css,fmt='%.8f')
    return True

if __name__ == '__main__':
    back_profile('control_points.dat','test.dat')
