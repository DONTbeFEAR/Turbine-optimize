# -*- coding: utf-8 -*-
"""
Created on Tue May 20 15:05:17 2014

@author: Eric
"""
import multiprocessing
import subprocess
import rotor_opt_main


def meshing(tmp):
    cmd = '\"C:\\Program Files\\ANSYS Inc\\v145\\TurboGrid\\bin\\cfxtg\" -batch \
          D:\\ShaoShuai\\863_Ire_Optimization\\%s' % tmp
    return(subprocess.call(cmd,shell=True))

def rotor1_mesh_parallel():
    gen_id = rotor_opt_main.generation_id
    popsize = 30
    ncpus = 2
    pool = multiprocessing.Pool(processes=ncpus)
    targets = ["generation%d\\individual%d\\rotor1_gen%d_id%d.tse"\
                %(gen_id,i,gen_id,i) for i in range(popsize)]
    mesh_results = [pool.apply_async(meshing,(input,)) for input in targets]
    pool.close()
    pool.join()

def stator5_mesh_parallel():
    gen_id = rotor_opt_main.generation_id
    popsize = 30
    ncpus = 2
    pool = multiprocessing.Pool(processes=ncpus)
    targets = ["generation%d\\individual%d\\stator5_gen%d_id%d.tse"\
                %(gen_id,i,gen_id,i) for i in range(popsize)]
    mesh_results = [pool.apply_async(meshing,(input,)) for input in targets]
    pool.close()
    pool.join()

def pre_processing(tmp):
    cmd = '\"C:\\Program Files\\ANSYS Inc\\v145\\CFX\\bin\\cfx5pre\" -batch\
           D:\\ShaoShuai\\863_Ire_Optimization\\%s' % tmp
    return(subprocess.call(cmd, shell=True))

def pre_parallel():
    gen_id = rotor_opt_main.generation_id
    popsize = 30
    ncpus = 10
    pool = multiprocessing.Pool(processes=ncpus)
    targets = ["generation%d\\individual%d\\gen%d_id%d.pre" %\
               (gen_id,i,gen_id,i) for i in range(popsize)]
    pre_results = [pool.apply_async(pre_processing,(input,)) for input in targets]
    pool.close()
    pool.join()

def solving(tmp):
    cmd = '\"D:\\ShaoShuai\\863_Ire_Optimization\\%s\"' % tmp
    return(subprocess.call(cmd, shell=True))

def solve_parallel():
    gen_id = rotor_opt_main.generation_id
    popsize = 30
    ncpus = 10
    pool = multiprocessing.Pool(processes=ncpus)
    targets = ["generation%d\\individual%d\\gen%d_id%d.bat" %\
               (gen_id,i,gen_id,i) for i in range(popsize)]
    solver_results = [pool.apply_async(solving,(input,)) for input in targets]
    pool.close()
    pool.join()

def post_processing(tmp):
    cmd = '\"C:\\Program Files\\ANSYS Inc\\v145\\CFX\\bin\\cfdpost\" -batch \
           D:\\ShaoShuai\\863_Ire_Optimization\\%s' % tmp
    return(subprocess.call(cmd, shell=True))

def post_parallel():
    gen_id = rotor_opt_main.generation_id
    popsize = 30
    ncpus = 10
    pool = multiprocessing.Pool(processes=ncpus)
    targets = ["generation%d\\individual%d\\gen%d_id%d.cse" %\
               (gen_id,i,gen_id,i) for i in range(popsize)]
    post_results = [pool.apply_async(post_processing,(input,)) for input in targets]
    pool.close()
    pool.join()

def stp_generating(tmp):
    cmd = '\"C:\Program Files\\ANSYS Inc\\v145\\Framework\\bin\\Win64\\runwb2\" -R \
           D:\\ShaoShuai\\863_Ire_Optimization\\%s' % tmp
    return(subprocess.call(cmd,shell=True))

def stp_parallel():
    gen_id = rotor_opt_main.generation_id
    popsize = 30
    ncpus = 2
    pool = multiprocessing.Pool(processes=ncpus)
    targets = ["generation%d\\individual%d\\stp_gen%d_id%d.wbjn"\
                %(gen_id,i,gen_id,i) for i in range(popsize)]
    mesh_results = [pool.apply_async(stp_generating,(input,)) for input in targets]
    pool.close()
    pool.join()

def FreeCAD_generating(tmp):
    cmd = '\"C:\\Program Files (x86)\\FreeCAD 0.14\\bin\\freecad\" \
           D:\\ShaoShuai\\863_Ire_Optimization\\%s' % tmp
    return(subprocess.call(cmd,shell=True))

def FreeCAD_parallel():
    gen_id = rotor_opt_main.generation_id
    popsize = 30
    ncpus = 10
    pool = multiprocessing.Pool(processes=ncpus)
    targets = ["generation%d\\individual%d\\FreeCAD_gen%d_id%d.FCMacro"\
                %(gen_id,i,gen_id,i) for i in range(popsize)]
    mesh_results = [pool.apply_async(FreeCAD_generating,(input,)) for input in targets]
    pool.close()
    pool.join()

def FEM_solving(tmp):
    cmd = '\"C:\\Program Files\\ANSYS Inc\\v145\\Framework\\bin\\Win64\\runwb2\" -R \
           D:\\ShaoShuai\\863_Ire_Optimization\\%s' % tmp
    return(subprocess.call(cmd,shell=True))

def FEM_parallel():
    gen_id = rotor_opt_main.generation_id
    popsize = 30
    ncpus = 10
    pool = multiprocessing.Pool(processes=ncpus)
    targets = ["generation%d\\individual%d\\FEM_gen%d_id%d.wbjn"\
                %(gen_id,i,gen_id,i) for i in range(popsize)]
    mesh_results = [pool.apply_async(FEM_solving,(input,)) for input in targets]
    pool.close()
    pool.join()

if __name__ == '__main__':
    pass
