# -*- coding: utf-8 -*-
"""
Created on Tue May 20 14:53:12 2014

@author: Eric
"""

def generator(random, args):
    """
    随机数生成器，用于实现静叶子午型线、安装角分布及厚度分布的扰动
    """
    size = args.get('num_input',47)
    return([random.uniform(-63.9, -58.1),
            random.uniform(-67.5, -62.5),
            random.uniform(-73.8, -70.2),
            random.uniform(-82.8, -81.2),
            random.uniform(2.7, 3.3),
            random.uniform(4.5378, 5.5462),
            random.uniform(5.0292, 6.1468),
            random.uniform(4.2777, 5.2283),
            random.uniform(2.6424, 3.2296),
            random.uniform(1.1115, 1.3585),

            random.uniform(34.1571, 47.4733    ),
            random.uniform(14.1829, 20.8410),
            random.uniform(0, 5.4127),
            random.uniform(16.2380, 27.0634),
            random.uniform(11.1829, 17.1829),
            random.uniform(29.2029, 35.7493),

            random.uniform(5.8370, 7.8370    ),
            random.uniform(45.8391, 51.3673),
            random.uniform(37.5470, 40.3111),
            random.uniform(6.8370, 11.1102),
            random.uniform(19.6565, 28.2029),
            random.uniform(34.5470, 40.5470),
            random.uniform(29.2029, 35.7493),

            random.uniform(1.9593, 2.3947    ),
            random.uniform(5.31, 6.49),
            random.uniform(18.1134, 22.1386),
            random.uniform(46.6434, 57.0086),

            random.uniform(3.6927, 4.5133    ),
            random.uniform(8.3979, 10.2641),
            random.uniform(26.7507, 32.6953),
            random.uniform(56.9376, 69.5904),

            random.uniform(6.0885, 7.4415    ),
            random.uniform(11.2636, 13.7544),
            random.uniform(37.0746, 45.3134),
            random.uniform(66.114, 80.806),

            random.uniform(1.0, 2.0    ),
            random.uniform(3.5, 4.5),
            random.uniform(4.5, 5.5),
            random.uniform(2.5, 3.5),
            random.uniform(1.0, 2.0),

            random.uniform(0.5, 1.0    ),
            random.uniform(0.5, 1.0),
            random.uniform(0.5, 1.0),
            random.uniform(0.5, 1.0),
            random.uniform(0.5, 1.0),

            random.uniform(-4, -0.5    ),
            random.uniform(-5.0, -1.0),
            random.uniform(-14.0, -4.0),
            random.uniform(14.1829, 18.0),
            random.uniform(14.1829, 16.0)])

if __name__ == '__main__':
    pass
