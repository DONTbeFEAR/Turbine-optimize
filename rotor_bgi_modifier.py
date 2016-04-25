# -*- coding: utf-8 -*-
"""
Created on Fri May 23 14:38:58 2014

@author: Eric
"""

def rotor1_bgi_modifier(cs,fname,wname):
    """
    根据candidate指定的参数修改静叶的参数化文件
    """
    f = open(fname,'rb')
    contents = f.readlines()
    f.close()
    #修改叶轮叶高
    contents[74] = contents[74].replace('6.837000000','%.8f'%cs[16],1)
    contents[75] = contents[75].replace('6.837000000','%.8f'%cs[16],1)
    contents[83] = contents[83].replace('6.837000000','%.8f'%cs[16],1)
    contents[84] = contents[84].replace('6.837000000','%.8f'%cs[16],1)
    contents[107] = contents[107].replace('6.837000000','%.8f'%cs[16],1)
    contents[129] = contents[129].replace('6.837000000','%.8f'%cs[16],1)
    #修改Hub控制点
    contents[52] = contents[52].replace('40.81520000','%.8f'%cs[10],1)
    contents[53] = contents[53].replace('14.18290000','%.8f'%cs[11],1)
    contents[53] = contents[53].replace('0.0000000000','%.8f'%cs[12],1)
    contents[54] = contents[54].replace('14.18290000','%.8f'%cs[14],1)
    contents[54] = contents[54].replace('21.65070000','%.8f'%cs[13],1)
    contents[55] = contents[55].replace('14.18290000','%.8f'%cs[14],1)
    contents[55] = contents[55].replace('32.47610000','%.8f'%cs[15],1)
    contents[63] = contents[63].replace('14.18290000','%.8f'%cs[14],1)
    contents[63] = contents[63].replace('32.47610000','%.8f'%cs[15],1)
    contents[64] = contents[64].replace('14.18290000','%.8f'%cs[14],1)
    #修改Shroud控制点
    contents[84] = contents[84].replace('45.83920000','%.8f'%cs[17],1)
    contents[85] = contents[85].replace('37.54700000','%.8f'%cs[18],1)
    contents[85] = contents[85].replace('6.837000000','%.8f'%cs[19],1)
    contents[86] = contents[86].replace('37.54700000','%.8f'%cs[21],1)
    contents[86] = contents[86].replace('23.92970000','%.8f'%cs[20],1)
    contents[87] = contents[87].replace('37.54700000','%.8f'%cs[21],1)
    contents[87] = contents[87].replace('32.47610000','%.8f'%cs[22],1)
    contents[95] = contents[95].replace('37.54700000','%.8f'%cs[21],1)
    contents[95] = contents[95].replace('32.47610000','%.8f'%cs[22],1)
    contents[96] = contents[96].replace('37.54700000','%.8f'%cs[21],1)
    #修改Hub&Shroud连接线
    contents[117] = contents[117].replace('14.18290000','%.8f'%cs[14],1)
    contents[118] = contents[118].replace('37.54700000','%.8f'%cs[21],1)
    contents[139] = contents[139].replace('14.18290000','%.8f'%cs[14],1)
    contents[139] = contents[139].replace('32.47610000','%.8f'%cs[15],1)
    contents[140] = contents[140].replace('37.54700000','%.8f'%cs[21],1)
    contents[140] = contents[140].replace('32.47610000','%.8f'%cs[22],1)
    #修改叶根厚度分布
    contents[267] = contents[267].replace('1.000000000','%.8f'%cs[35],1)
    contents[268] = contents[268].replace('3.851920435','%.8f'%cs[36],1)
    contents[269] = contents[269].replace('5.004879457','%.8f'%cs[37],1)
    contents[270] = contents[270].replace('2.779786374','%.8f'%cs[38],1)
    contents[271] = contents[271].replace('1.353660000','%.8f'%cs[39],1)
    #修改叶顶厚度分布
    contents[285] = contents[285].replace('0.7264810000','%.8f'%cs[40],1)
    contents[286] = contents[286].replace('0.9351931626','%.8f'%cs[41],1)
    contents[287] = contents[287].replace('0.9886868091','%.8f'%cs[42],1)
    contents[288] = contents[288].replace('0.7981683016','%.8f'%cs[43],1)
    contents[289] = contents[289].replace('0.5000000000','%.8f'%cs[44],1)
    #修改叶片beta角分布
    contents[203] = contents[203].replace('2.177251080','%.8f'%cs[23],1)
    contents[204] = contents[204].replace('5.899790159','%.8f'%cs[24],1)
    contents[205] = contents[205].replace('20.12614209','%.8f'%cs[25],1)
    contents[206] = contents[206].replace('51.82592333','%.8f'%cs[26],1)
    contents[224] = contents[224].replace('4.103000000','%.8f'%cs[27],1)
    contents[225] = contents[225].replace('9.331000000','%.8f'%cs[28],1)
    contents[226] = contents[226].replace('29.72300000','%.8f'%cs[29],1)
    contents[227] = contents[227].replace('63.26400000','%.8f'%cs[30],1)
    contents[245] = contents[245].replace('6.764581960','%.8f'%cs[31],1)
    contents[246] = contents[246].replace('12.50382627','%.8f'%cs[32],1)
    contents[247] = contents[247].replace('41.19422277','%.8f'%cs[33],1)
    contents[248] = contents[248].replace('73.46000000','%.8f'%cs[34],1)


    w = open(wname,'wb')
    w.writelines(contents)
    w.close()
    return(True)

if __name__ == '__main__':
    pass
