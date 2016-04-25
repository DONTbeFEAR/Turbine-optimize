# -*- coding: utf-8 -*-
"""
Created on Fri May 23 16:23:00 2014

@author: Eric
"""

def stator5_tse_modifier(fname,wname):
    """
    修改.tse网格生成脚本文件
    """
    f = open(fname,'r')
    contents = f.read()
    f.close()
    ind_path = wname[:wname.rfind('\\')]
    contents = contents.replace('stator.inf',ind_path+'\\BladeGen.inf',1)
    contents = contents.replace('stator.tst',wname[:-3]+'tst',1)
    contents = contents.replace('stator.gtm',wname[:-3]+'gtm',1)
    w = open(wname,'w')
    w.write(contents)
    w.close()
    return(True)

if __name__ == '__main__':
    pass
