# -*- coding: utf-8 -*-
"""
Created on Tue May 20 15:44:32 2014

@author: Eric
"""

from time import time
from time import sleep
from random import Random
from inspyred import ec
from generator import *
from bounder import *
from evaluator import *
from my_terminator import *

generation_id = 0

def main(prng=None, display=False):
    if prng is None:
        prng = Random()
    max_gens = 500

    if os.path.exists('ec0.pkl'):
        with open('ec0.pkl','rb') as pickle_file:
            population = pickle.load(pickle_file)
            archive = pickle.load(pickle_file)
            random_state = pickle.load(pickle_file)
            num_generations = pickle.load(pickle_file)
            num_evaluations = pickle.load(pickle_file)
            prng.setstate(random_state)

            stat_file = open('ga_statistics.csv','w')
            ind_file = open('ga_individuals.csv','w')
            ea = ec.emo.NSGA2(prng)
            ea.variator = [inspyred.ec.variators.blend_crossover,
                           inspyred.ec.variators.gaussian_mutation]
            ea.observer = [inspyred.ec.observers.file_observer,
                           inspyred.ec.observers.archive_observer,
                           inspyred.ec.observers.stats_observer]
            ea.terminator = [inspyred.ec.terminators.generation_termination,
                             my_terminator]
            ea.num_evaluations = num_evaluations
            ea.num_generations = num_generations
            ea.archive = archive

            final_pop = ea.evolve(seeds=[p.candidate for p in population],
                                  generator=generator,
                                  evaluator=evaluator,
                                  pop_size=30,
                                  maximize=True,
                                  bounder=bounder,
                                  max_generations= max_gens-num_generations,
                                  num_elites=2,
                                  statistics_file=stat_file,
                                  individuals_file=ind_file)
            stat_file.close()
            ind_file.close()
    else:
        prng.seed(1234)
        stat_file = open('ga_statistics.csv', 'w')
        ind_file = open('ga_individuals.csv', 'w')
        ea = ec.emo.NSGA2(prng)
        ea.variator = [inspyred.ec.variators.blend_crossover,
                       inspyred.ec.variators.gaussian_mutation]
        ea.observer = [inspyred.ec.observers.file_observer,
                       inspyred.ec.observers.archive_observer,
                       inspyred.ec.observers.stats_observer]
        ea.terminator = [inspyred.ec.terminators.generation_termination,
                         my_terminator]

        final_pop = ea.evolve(generator=generator,
                              evaluator=evaluator,
                              pop_size=30,
                              maximize=True,
                              bounder=bounder,
                              max_generations=max_gens,
                              num_elites=2,
                              statistics_file=stat_file,
                              individuals_file=ind_file)
        stat_file.close()
        ind_file.close()

    if display:
        # Sort and print the best individual, who will be at index 0.
        final_pop.sort(reverse=True)
        print('Terminated due to %s.' % ea.termination_cause)
        print(final_pop[0])
    return ea

if __name__ == '__main__':
    main(display=False)