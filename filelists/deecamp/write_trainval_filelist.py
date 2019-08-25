import numpy as np
from os import listdir
from os.path import isfile, isdir, join
import os
import json
import random

cwd = os.getcwd() 
data_path = join(cwd,'new_train')
savedir = './'
dataset_list = ['base','val','novel']

#if not os.path.exists(savedir):
#    os.makedirs(savedir)

folder_list = [f for f in listdir(data_path) if isdir(join(data_path, f))]
folder_list.sort()
label_dict = dict(zip(folder_list,range(0,len(folder_list))))

classfile_list_all = []
for i, folder in enumerate(folder_list):
    folder_path = join(data_path, folder)
    classfile_list_all.append([join(folder_path,cf) for cf in listdir(folder_path) if (isfile(join(folder_path, cf)) and cf[0] != ".")])
    random.shuffle(classfile_list_all[i])

for dataset in dataset_list:
    file_list = []
    label_list = []
    for i,classfile_list in enumerate(classfile_list_all):
        cla = classfile_list[0].split("/")[-2].split("_")[0]
        if "base" in dataset:
            #if str(cla) in ["bottle","cable","capsule","hazelnut","pill","screw","toothbrush","transistor","zipper"]:
            #if i in range(12):
            if str(cla) not in ["metal","carpet"]:
                file_list = file_list + classfile_list
                label_list = label_list + np.repeat(i, len(classfile_list)).tolist()
                #print(file_list)
                #print(label_list)
        if 'val' in dataset:
            if str(cla) in ["metal"]:
            #if i in range(12,18):
                file_list = file_list + classfile_list
                label_list = label_list + np.repeat(i, len(classfile_list)).tolist()
                print(file_list)
        if 'novel' in dataset:
            if str(cla) in ["metal","carpet"]:
            #if i in range(18,24):
                file_list = file_list + classfile_list
                label_list = label_list + np.repeat(i, len(classfile_list)).tolist()
                #print(label_list)
    fo = open(savedir + dataset + ".json", "w")
    fo.write('{"label_names": [')
    fo.writelines(['"%s",' % item  for item in folder_list])
    fo.seek(0, os.SEEK_END) 
    fo.seek(fo.tell()-1, os.SEEK_SET)
    fo.write('],')

    fo.write('"image_names": [')
    fo.writelines(['"%s",' % item  for item in file_list])
    fo.seek(0, os.SEEK_END) 
    fo.seek(fo.tell()-1, os.SEEK_SET)
    fo.write('],')

    fo.write('"image_labels": [')
    fo.writelines(['%d,' % item  for item in label_list])
    fo.seek(0, os.SEEK_END) 
    fo.seek(fo.tell()-1, os.SEEK_SET)
    fo.write(']}')

    fo.close()
    print("%s -OK" %dataset)
