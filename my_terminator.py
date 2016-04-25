# -*- coding: utf-8 -*-
"""
Created on Tue May 20 16:10:37 2014

@author: Eric
"""

import pickle

def my_terminator(population, num_generations, num_evaluations, args):
    """ 每完成一代就保存一个.pkl文件，以便续算 """
    if num_generations:
        with open('ec%d.pkl' % num_generations, 'wb') as pickle_file:
            random_state = args['_ec']._random.getstate()
            archive = args['_ec'].archive
            pickle.dump(population, pickle_file, -1)
            pickle.dump(archive, pickle_file, -1)
            pickle.dump(random_state, pickle_file, -1)
            pickle.dump(num_generations, pickle_file, -1)
            pickle.dump(num_evaluations, pickle_file, -1)
    return(False)

if __name__ == '__main__':
    pass