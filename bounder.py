# -*- coding: utf-8 -*-
"""
Created on Tue May 20 14:57:48 2014

@author: Eric
"""

def bounder(candidate, args):
    """
    用于约束优化算法产生的扰动范围，防止扰动超出给定的范围
    """
    bound = [[-63.9, -58.1],
             [-67.5, -62.5],
             [-73.8, -70.2],
             [-82.8, -81.2],
             [2.7, 3.3],
             [4.5378, 5.5462],
             [5.0292, 6.1468],
             [4.2777, 5.2283],
             [2.6424, 3.2296],
             [1.1115, 1.3585],
             [34.1571, 47.4733],
             [14.1829, 20.8410],
             [0.0000, 5.4127],
             [16.2380, 27.0634],
             [11.1829, 17.1829],
             [29.2029, 35.7493],
             [5.8370, 7.8370],
             [45.8391, 51.3673],
             [37.5470, 40.3111],
             [6.8370, 11.1102],
             [19.6565, 28.2029],
             [34.5470, 40.5470],
             [29.2029, 35.7493],
             [1.9593, 2.3947],
             [5.31, 6.49],
             [18.1134, 22.1386],
             [46.6434, 57.0086],
             [3.6927, 4.5133],
             [8.3979, 10.2641],
             [26.7507, 32.6953],
             [56.9376, 69.5904],
             [6.0885, 7.4415],
             [11.2636, 13.7544],
             [37.0746, 45.3134],
             [66.114, 80.806],
             [1.0, 2.0],
             [3.5, 4.5],
             [4.5, 5.5],
             [2.5, 3.5],
             [1.0, 2.0],
             [0.5, 1.0],
             [0.5, 1.0],
             [0.5, 1.0],
             [0.5, 1.0],
             [0.5, 1.0],
             [-4.0, -0.5],
             [-5.0, -1.0],
             [-14.0, -4.0],
             [14.1829, 18.0],
             [14.1829, 16.0]]
    for i,c in enumerate(candidate):
        tmp = max(min(c,bound[i][1]),bound[i][0])
        candidate[i] = tmp
    return(candidate)

if __name__  == '__main__':
    pass
