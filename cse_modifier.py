# -*- coding: utf-8 -*-
"""
Created on Fri May 23 16:40:08 2014

@author: Eric
"""

def cse_modifier(fname,wname):
    """
    fuck!
    """
    f = open(fname,'r')
    contents = f.read()
    f.close()
    ind_path = wname[:wname.rfind('\\')]
    contents = contents.replace('stage_001.res',wname[:-4]+'_001.res')
    contents = contents.replace('export.csv',ind_path+'\\export.csv')
    w = open(wname,'w')
    w.write(contents)
    w.close()
    return(True)

if __name__ == '__main__':
    pass
