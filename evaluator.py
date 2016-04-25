# -*- coding: utf-8 -*-
"""
Created on Tue May 20 16:11:47 2014

@author: Eric
"""
import os
import shutil
import subprocess
import inspyred
import rotor_opt_main
from parallel_controller import rotor_mesh_parallel
from parallel_controller import stator_mesh_parallel
from parallel_controller import pre_parallel
from parallel_controller import solve_parallel
from parallel_controller import post_parallel
from rotor_bgi_modifier import rotor_bgi_modifier
from stator_bgi_modifier import stator_bgi_modifier
from rotor_tse_modifier import rotor_tse_modifier
from stator_tse_modifier import stator_tse_modifier
from pre_modifier import pre_modifier
from cse_modifier import cse_modifier
from back_profile import back_profile

def evaluator(candidates, args):
    """
    评价函数，返回适应度值
    """
    gen_id = rotor_opt_main.generation_id
    generation = "generation%d" % gen_id
    #创建保存第n代个体的文件夹
    root_path = "D:\\ShaoShuai\\863_Ire_Optimization"
    gen_path = root_path + "\\%s" % generation
    os.mkdir(gen_path)


    #Begin the .curve files generation
    for ind_id, cs in enumerate(candidates):
        individual = "individual%d" % ind_id
        ind_path = root_path + "\\%s\\%s" % (generation,individual)
        fname1 = "rotor.bgi"
        fname2 = "rotor_gen%d_id%d.bgi"%(gen_id,ind_id)
        #创建保存第n个个体的文件夹
        os.mkdir(ind_path)
        #修改叶栅的参数化脚本
        rotor_bgi_modifier(cs,root_path+"\\%s"%fname1,ind_path+"\\%s"%fname2)
        #生成叶栅的.curve文件
        e = os.path.exists(ind_path+"\\BladeGen.inf")
        while not e:
            subprocess.call('\"C:\\Program Files\\ANSYS Inc\\v145\\aisol\\BladeModeler\\BladeGen\\BladeBatch\" \
                            %s\\%s -TG %s'%(ind_path,fname2,ind_path),shell=True)
            e = os.path.exists(ind_path+"\\BladeGen.inf")
    #End the .curve files generation


    #Begin the mesh generation
    for ind_id, cs in enumerate(candidates):
        individual = "individual%d" % ind_id
        ind_path = root_path + "\\%s\\%s" % (generation,individual)
        fname5 = "rotor.tse"
        fname6 = "rotor_gen%d_id%d.tse"%(gen_id,ind_id)

        #修改网格生成脚本
        rotor_tse_modifier(root_path+"\\%s"%fname5,ind_path+"\\%s"%fname6)

    rotor_mesh_parallel()

    for ind_id, cs in enumerate(candidates):
        individual = "individual%d" % ind_id
        ind_path = root_path + "\\%s\\%s" % (generation,individual)
        fname6 = "rotor_gen%d_id%d.tse"%(gen_id,ind_id)
        fname9 = "rotor_gen%d_id%d.gtm"%(gen_id,ind_id)
        e = os.path.exists(ind_path+"\\%s"%fname9)
        while not e:
            subprocess.call('\"C:\\Program Files\\ANSYS Inc\\v145\\TurboGrid\\bin\\cfxtg\" -batch \
                            %s\\%s'%(ind_path,fname6),shell=True)
            e = os.path.exists(ind_path+"\\%s"%fname9)
    #删除BladeGen.inf文件
    for ind_id, cs in enumerate(candidates):
        individual = "individual%d" % ind_id
        ind_path = root_path + "\\%s\\%s" % (generation,individual)
        os.remove(ind_path+"\\BladeGen.inf")


#生成静叶网格
    for ind_id, cs in enumerate(candidates):
        individual = "individual%d" % ind_id
        ind_path = root_path + "\\%s\\%s" % (generation,individual)
        fname3 = "stator.bgi"
        fname4 = "stator_gen%d_id%d.bgi"%(gen_id,ind_id)
        #修改叶栅的参数化脚本
        stator_bgi_modifier(cs,root_path+"\\%s"%fname3,ind_path+"\\%s"%fname4)
        #生成叶栅的.curve文件
        e = os.path.exists(ind_path+"\\BladeGen.inf")
        while not e:
            subprocess.call('\"C:\\Program Files\\ANSYS Inc\\v145\\aisol\\BladeModeler\\BladeGen\\BladeBatch\" \
                            %s\\%s -TG %s'%(ind_path,fname4,ind_path),shell=True)
            e = os.path.exists(ind_path+"\\BladeGen.inf")

    #Begin the mesh generation
    for ind_id, cs in enumerate(candidates):
        individual = "individual%d" % ind_id
        ind_path = root_path + "\\%s\\%s" % (generation,individual)
        fname7 = "stator.tse"
        fname8 = "stator_gen%d_id%d.tse"%(gen_id,ind_id)

        #修改网格生成脚本
        stator_tse_modifier(root_path+"\\%s"%fname7,ind_path+"\\%s"%fname8)

    stator_mesh_parallel()


    for ind_id, cs in enumerate(candidates):
        individual = "individual%d" % ind_id
        ind_path = root_path + "\\%s\\%s" % (generation,individual)
        fname8 = "stator_gen%d_id%d.tse"%(gen_id,ind_id)
        fname10 = "stator_gen%d_id%d.gtm"%(gen_id,ind_id)
        e = os.path.exists(ind_path+"\\%s"%fname10)
        while not e:
            subprocess.call('\"C:\\Program Files\\ANSYS Inc\\v145\\TurboGrid\\bin\\cfxtg\" -batch \
                            %s\\%s'%(ind_path,fname8),shell=True)
            e = os.path.exists(ind_path+"\\%s"%fname10)
    #End the mesh generation


    #Begin the .pre file generation
    for ind_id, cs in enumerate(candidates):
        individual = "individual%d" % ind_id
        ind_path = root_path + "\\%s\\%s" % (generation,individual)
        fname11 = "stage.pre"
        fname12 = "gen%d_id%d.pre"%(gen_id,ind_id)
        pre_modifier(root_path+"\\%s"%fname11,ind_path+"\\%s"%fname12)
    #End the .pre file generation

    #Begin the .def file parallel generation
    pre_parallel()
    for ind_id, cs in enumerate(candidates):
        individual = "individual%d" % ind_id
        ind_path = root_path + "\\%s\\%s" % (generation,individual)
        fname12 = "gen%d_id%d.pre"%(gen_id,ind_id)
        fname13 = "gen%d_id%d.def"%(gen_id,ind_id)
        e = os.path.exists(ind_path+"\\%s"%fname13)
        while not e:
            subprocess.call('\"C:\\Program Files\\ANSYS Inc\\v145\\CFX\\bin\\cfx5pre\" -batch \
                            %s\\%s'%(ind_path,fname12),shell=True)
            e = os.path.exists(ind_path+"\\%s"%fname13)
    #End the .def file parallel generation

    #Begin solving
    for ind_id, cs in enumerate(candidates):
        individual = "individual%d" % ind_id
        ind_path = root_path + "\\%s\\%s" % (generation,individual)
        fname13 = "gen%d_id%d.def"%(gen_id,ind_id)
        fname14 = "gen%d_id%d.bat"%(gen_id,ind_id)
        w = open('%s\\%s'%(ind_path,fname14),'w')
        w.writelines('cd %s\n\"C:\\Program Files\\Ansys Inc\\v145\\CFX\\bin\\cfx5solve\" -def %s'%(ind_path,fname13))
        w.close()
    solve_parallel()
    for ind_id, cs in enumerate(candidates):
        individual = "individual%d" % ind_id
        ind_path = root_path + "\\%s\\%s" % (generation,individual)
        fname14 = "gen%d_id%d.bat"%(gen_id,ind_id)
        fname15 = "gen%d_id%d_001.res"%(gen_id,ind_id)
        e = os.path.exists(ind_path+"\\%s"%fname15)
        while not e:
            subprocess.call('\"%s\\%s\"'%(ind_path,fname14),shell=True)
            e = os.path.exists(ind_path+"\\%s"%fname15)
    #End solving

    #Begin the .cse file generation
    for ind_id, cs in enumerate(candidates):
        individual = "individual%d" % ind_id
        ind_path = root_path + "\\%s\\%s" % (generation,individual)
        fname16 = "stage.cse"
        fname17 = "gen%d_id%d.cse"%(gen_id,ind_id)
        e = os.path.exists(ind_path+"\\%s"%fname17)
        while not e:
            cse_modifier(root_path+"\\%s"%fname16,ind_path+"\\%s"%fname17)
            e = os.path.exists(ind_path+"\\%s"%fname17)

    #End the .cse file generation
    post_parallel()
    for ind_id, cs in enumerate(candidates):
        individual = "individual%d" % ind_id
        ind_path = root_path + "\\%s\\%s" % (generation,individual)
        fname17 = "gen%d_id%d.cse"%(gen_id,ind_id)
        fname18 = "export.csv"
        e = os.path.exists(ind_path+"\\%s"%fname18)
        while not e:
            subprocess.call('\"C:\\Program Files\\ANSYS Inc\\v145\\CFX\\bin\\cfdpost\" -batch \
                            %s\\%s'%(ind_path,fname17),shell=True)
            e = os.path.exists(ind_path+"\\%s"%fname18)
    #删除.res文件
    for ind_id, cs in enumerate(candidates):
        individual = "individual%d" % ind_id
        ind_path = root_path + "\\%s\\%s" % (generation,individual)
        fname15 = "gen%d_id%d_001.res"%(gen_id,ind_id)
        os.remove(ind_path+"\\"+fname15)

    #Begin the FEM
    for ind_id, cs in enumerate(candidates):
        individual = "individual%d" % ind_id
        ind_path = root_path + "\\%s\\%s" % (generation,individual)
        #修改叶轮bgi文件，改成CutOff进口，并适当延长进口
        f = open('%s\\rotor_gen%d_id%d.bgi'%(ind_path,gen_id,ind_id),'rb')
        contents = f.readlines()
        f.close()
        contents[43] = contents[43].replace('54.13130000','54.63130000',1)
        contents[51] = contents[51].replace('54.13130000','54.63130000',1)
        contents[75] = contents[75].replace('54.13130000','54.63130000',1)
        contents[83] = contents[83].replace('54.13130000','54.63130000',1)
        contents[128] = contents[128].replace('54.13130000','54.63130000',1)
        contents[129] = contents[129].replace('54.13130000','54.63130000',1)
        contents[179] = contents[179].replace('Ellipse','CutOff',1)
        contents.pop(180)
        contents.pop(180)
        contents[181] = contents[181].replace('2.000000000','1.0',1)
        contents[182] = contents[182].replace('2.000000000','1.0',1)
        w = open('%s\\FEM_gen%d_id%d.bgi'%(ind_path,gen_id,ind_id),'wb')
        w.writelines(contents)
        w.close()
        #由bgi文件生成bgd文件
        e = os.path.exists('%s\\FEM_gen%d_id%d.bgd'%(ind_path,gen_id,ind_id))
        while not e:
            subprocess.call('\"C:\\Program Files\\ANSYS Inc\\v145\\aisol\\BladeModeler\\BladeGen\\BladeBatch\" \
                             %s\\FEM_gen%d_id%d.bgi %s\\FEM_gen%d_id%d.bgd'%(ind_path,gen_id,ind_id,ind_path,gen_id,ind_id))
            e = os.path.exists('%s\\FEM_gen%d_id%d.bgd'%(ind_path,gen_id,ind_id))
        #修改stp几何文件生成脚本
        f = open('bgd2stp.wbjn','rb')
        contents = f.readlines()
        f.close()
        contents[5] = contents[5].replace('rotorforFEM.bgd',r'%s\\FEM_gen%d_id%d.bgd'%(repr(ind_path).strip('\''),gen_id,ind_id),1)
        contents[8] = contents[8].replace('rotorforFEM.stp',r'%s\\FEM_gen%d_id%d.stp'%(repr(ind_path).strip('\''),gen_id,ind_id),1)
        w = open('%s\\stp_gen%d_id%d.wbjn'%(ind_path,gen_id,ind_id),'wb')
        w.writelines(contents)
        w.close()
        e = os.path.exists('%s\\FEM_gen%d_id%d.stp'%(ind_path,gen_id,ind_id))
        while not e:
            subprocess.call('\"C:\\Program Files\\ANSYS Inc\\v145\\Framework\\bin\\Win64\\runwb2\" -R %s\\stp_gen%d_id%d.wbjn'%(ind_path,gen_id,ind_id))
            e = os.path.exists('%s\\FEM_gen%d_id%d.stp'%(ind_path,gen_id,ind_id))

        #生成轮背型线的型值点
        f = open('control_points.dat','rb')
        contents = f.readlines()
        f.close()
        contents[1] = contents[1].replace('-3.72819281',str(cs[45]),1)
        contents[2] = contents[2].replace('-4.70676819',str(cs[46]),1)
        contents[3] = contents[3].replace('-9.76959548',str(cs[47]),1)
        contents[3] = contents[3].replace('16.36695170',str(cs[48]),1)
        contents[4] = contents[4].replace('13.59145474',str(cs[49]),1)
        w = open('%s\\ControlPoints_gen%d_id%d.dat'%(ind_path,gen_id,ind_id),'wb')
        w.writelines(contents)
        w.close()
        back_profile('%s\\ControlPoints_gen%d_id%d.dat'%(ind_path,gen_id,ind_id),'%s\\CS_gen%d_id%d.dat'%(ind_path,gen_id,ind_id))



        #调用freeCAD进行几何处理
        f = open('rotor_FreeCAD.FCMacro','rb')
        contents = f.read()
        f.close()
        contents = contents.replace('rotorforFEM.stp',r'%s\\FEM_gen%d_id%d.stp'%(repr(ind_path).strip('\''),gen_id,ind_id),1)
        contents = contents.replace('curve_points.dat',r'%s\\CS_gen%d_id%d.dat'%(repr(ind_path).strip('\''),gen_id,ind_id),1)
        contents = contents.replace('rotorforFEM_modified.stp',r'%s\\FEMmodified_gen%d_id%d.stp'%(repr(ind_path).strip('\''),gen_id,ind_id),1)
        w = open('%s\\FreeCAD_gen%d_id%d.FCMacro'%(ind_path,gen_id,ind_id),'wb')
        w.writelines(contents)
        w.close()
        e = os.path.exists('%s\\FEMmodified_gen%d_id%d.stp'%(ind_path,gen_id,ind_id))
        while not e:
            subprocess.call('\"C:\\Program Files (x86)\\FreeCAD 0.14\\bin\\freecad\" %s\\FreeCAD_gen%d_id%d.FCMacro'%(ind_path,gen_id,ind_id))
            e = os.path.exists('%s\\FEMmodified_gen%d_id%d.stp'%(ind_path,gen_id,ind_id))



        #修改FEM计算脚本
        f = open('rotorFEM.wbjn','rb')
        contents = f.readlines()
        f.close()
        contents[12] = contents[12].replace('test',r'%s'%repr(ind_path).strip('\''),1)
        contents[15] = contents[15].replace('rotorforFEM_modified.stp',r'%s\\FEMmodified_gen%d_id%d.stp'%(repr(ind_path).strip('\''),gen_id,ind_id),1)
        contents[18] = contents[18].replace('GeometryReplace.log',r'%s\\FEM_gen%d_id%d.log'%(repr(ind_path).strip('\''),gen_id,ind_id),1)
        w = open('%s\\FEM_gen%d_id%d.wbjn'%(ind_path,gen_id,ind_id),'wb')
        w.writelines(contents)
        w.close()

        e = os.path.exists('%s\\FEM_gen%d_id%d.log'%(ind_path,gen_id,ind_id))
        while not e:
            subprocess.call('\"C:\\Program Files\\ANSYS Inc\\v145\\Framework\\bin\\Win64\\runwb2\" -R %s\\FEM_gen%d_id%d.wbjn'%(ind_path,gen_id,ind_id))
            e = os.path.exists('%s\\FEM_gen%d_id%d.log'%(ind_path,gen_id,ind_id))

        f = open('%s\\FEM_gen%d_id%d.log'%(ind_path,gen_id,ind_id),'rb')
        staff = f.readlines()
        f.close()
        try:
            e2 = staff[5][34].isdigit()
        except:
            e2 = False
        if not e2:
            f = open('rotorFEM-Case2.wbjn','rb')
            contents = f.readlines()
            f.close()
            contents[12] = contents[12].replace('test',r'%s'%repr(ind_path).strip('\''),1)
            contents[15] = contents[15].replace('rotorforFEM_modified.stp',r'%s\\FEMmodified_gen%d_id%d.stp'%(repr(ind_path).strip('\''),gen_id,ind_id),1)
            contents[18] = contents[18].replace('GeometryReplace.log',r'%s\\FEM_gen%d_id%d.log'%(repr(ind_path).strip('\''),gen_id,ind_id),1)
            w = open('%s\\FEM_gen%d_id%d.wbjn'%(ind_path,gen_id,ind_id),'wb')
            w.writelines(contents)
            w.close()
            subprocess.call('\"C:\\Program Files\\ANSYS Inc\\v145\\Framework\\bin\\Win64\\runwb2\" -R %s\\FEM_gen%d_id%d.wbjn'%(ind_path,gen_id,ind_id))

        f = open('%s\\FEM_gen%d_id%d.log'%(ind_path,gen_id,ind_id),'rb')
        staff = f.readlines()
        f.close()
        try:
            e2 = staff[5][34].isdigit()
        except:
            e2 = False
        if not e2:
            f = open('rotorFEM-Case3.wbjn','rb')
            contents = f.readlines()
            f.close()
            contents[12] = contents[12].replace('test',r'%s'%repr(ind_path).strip('\''),1)
            contents[15] = contents[15].replace('rotorforFEM_modified.stp',r'%s\\FEMmodified_gen%d_id%d.stp'%(repr(ind_path).strip('\''),gen_id,ind_id),1)
            contents[18] = contents[18].replace('GeometryReplace.log',r'%s\\FEM_gen%d_id%d.log'%(repr(ind_path).strip('\''),gen_id,ind_id),1)
            w = open('%s\\FEM_gen%d_id%d.wbjn'%(ind_path,gen_id,ind_id),'wb')
            w.writelines(contents)
            w.close()
            subprocess.call('\"C:\\Program Files\\ANSYS Inc\\v145\\Framework\\bin\\Win64\\runwb2\" -R %s\\FEM_gen%d_id%d.wbjn'%(ind_path,gen_id,ind_id))

        f = open('%s\\FEM_gen%d_id%d.log'%(ind_path,gen_id,ind_id),'rb')
        staff = f.readlines()
        f.close()
        try:
            e2 = staff[5][34].isdigit()
        except:
            e2 = False
        if not e2:
            shutil.copy('FEM.log','%s\\FEM_gen%d_id%d.log'%(ind_path,gen_id,ind_id))


    #读取计算结果，并返回适应度值
    fitness = []
    for ind_id, cs in enumerate(candidates):
        individual = "individual%d" % ind_id
        ind_path = root_path + "\\%s\\%s" % (generation,individual)
        fname19 = "export.csv"
        f = open(ind_path+"\\%s"%fname19,'r')
        i = 6
        while i:
            content1 = f.readline()
            i-=1
        content1 = f.readline().strip(' \n').replace(', ','\t')
        content1 = [float(data) for data in content1.split('\t')]
        f.close()
        effts = content1[0]
        masscon = 1.0/(abs(content1[1] - 1.00265)*100)
        f = open('%s\\FEM_gen%d_id%d.log'%(ind_path,gen_id,ind_id))
        content2 = f.readlines()
        f.close()
        maxstress = float(content2[5][34:42])
        massrotor = float(content2[6][22:28])
        fitness.append(inspyred.ec.emo.Pareto([effts,masscon,1.0/massrotor,1.0/maxstress*1000]))
    rotor_opt_main.generation_id += 1
    return(fitness)

if __name__ == '__main__':
    pass









