# -*- coding: utf-8 -*-
"""
Created on Fri May 23 16:23:00 2014

@author: Eric
"""

def pre_modifier(fname,wname):
    """
    修改.pre文件，使得前处理锁定正确的网格文件
    """
    f = open(fname,'r')
    contents = f.read()
    f.close()
    ind_path = wname[:wname.rfind('\\')]
    name1 = ind_path+"\\"+"stator_"+wname[wname.rfind('\\')+1:-3]+'gtm'
    name2 = ind_path+"\\"+"rotor_"+wname[wname.rfind('\\')+1:-3]+'gtm'
    contents = contents.replace('stator.gtm',name1,1)
    contents = contents.replace('rotor.gtm',name2,1)
    contents = contents.replace('stage.cfx',wname[:-3]+'cfx',1)
    contents = contents.replace('stage.def',wname[:-3]+'def',1)
    w = open(wname,'w')
    w.write(contents)
    w.close()
    return(True)

if __name__ == '__main__':
    pass