# -*- coding: utf-8 -*-
"""
Created on Fri May 23 14:38:58 2014

@author: Eric
"""

def stator5_bgi_modifier(cs,fname,wname):
    """
    根据candidate指定的参数修改静叶的参数化文件
    """
    f = open(fname,'rb')
    contents = f.readlines()
    f.close()
    #修改喷嘴叶高
    contents[74] = contents[74].replace('6.837000000','%.8f'%cs[16],1)
    contents[75] = contents[75].replace('6.837000000','%.8f'%cs[16],1)
    contents[83] = contents[83].replace('6.837000000','%.8f'%cs[16],1)
    contents[84] = contents[84].replace('6.837000000','%.8f'%cs[16],1)
    contents[85] = contents[85].replace('6.837000000','%.8f'%cs[16],1)
    contents[86] = contents[86].replace('6.837000000','%.8f'%cs[16],1)
    contents[87] = contents[87].replace('6.837000000','%.8f'%cs[16],1)
    contents[95] = contents[95].replace('6.837000000','%.8f'%cs[16],1)
    contents[96] = contents[96].replace('6.837000000','%.8f'%cs[16],1)
    contents[107] = contents[107].replace('6.837000000','%.8f'%cs[16],1)
    contents[118] = contents[118].replace('6.837000000','%.8f'%cs[16],1)
    contents[129] = contents[129].replace('6.837000000','%.8f'%cs[16],1)
    contents[140] = contents[140].replace('6.837000000','%.8f'%cs[16],1)
    #修改喷嘴叶片角
    contents[191] = contents[191].replace('-60.99995166','%.8f'%cs[0],1)
    contents[192] = contents[192].replace('-64.99977003','%.8f'%cs[1],1)
    contents[193] = contents[193].replace('-72.00016837','%.8f'%cs[2],1)
    contents[194] = contents[194].replace('-82.00000077','%.8f'%cs[3],1)
    #修改喷嘴厚度
    contents[213] = contents[213].replace('3.000000000','%.8f'%cs[4],1)
    contents[214] = contents[214].replace('5.041560000','%.8f'%cs[5],1)
    contents[215] = contents[215].replace('5.588260000','%.8f'%cs[6],1)
    contents[216] = contents[216].replace('4.753000000','%.8f'%cs[7],1)
    contents[217] = contents[217].replace('2.936410000','%.8f'%cs[8],1)
    contents[218] = contents[218].replace('1.234890000','%.8f'%cs[9],1)

    w = open(wname,'wb')
    w.writelines(contents)
    w.close()
    return(True)

if __name__ == '__main__':
    pass
