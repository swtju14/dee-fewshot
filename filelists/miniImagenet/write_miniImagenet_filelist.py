import numpy as np
from os import listdir
from os.path import isfile, isdir, join
import os
import json
import random
import re
import glob

cwd = os.getcwd() 
data_path = join(cwd,'mini-imagenet/images/')
savedir = './'
dataset_list = ['base', 'val', 'novel']

#if not os.path.exists(savedir):
#    os.makedirs(savedir)

cl = -1
folderlist = []

datasetmap = {'base':'train','val':'val','novel':'test'};
filelists = {'base':{},'val':{},'novel':{} }
filelists_flat = {'base':[],'val':[],'novel':[] }
labellists_flat = {'base':[],'val':[],'novel':[] }

for dataset in dataset_list:
    with open('mini-imagenet/' + datasetmap[dataset] + ".csv", "r") as lines:
        fids = []
        labels = []
        for i, line in enumerate(lines):
            if i == 0:
                continue
            fid, _ , label = re.split(',|\.', line)
            label = label.replace('\n','')
            fids.append(fid)
            labels.append(label)
        for fid,label in zip(fids,labels):
            if not label in filelists[dataset]:
                folderlist.append(label)
                #filelists[dataset][label] = []
                #fname = []
            for label in list(set(labels)):
                filelists[dataset][label] = []
                fname = []
                if fid[:9] == label:
                #print(label,fid)
                    fname.append(join(data_path,fid+".jpg"))
            print(fname)
            filelists[dataset][label].append(fname)


                #fname = []
                #fnames = listdir( join(data_path ))
                #fname_number = [ int(re.split('_|\.', fname)[1]) for fname in fnames]
                #sorted_fnames = list(zip( *sorted(  zip(fnames, fname_number), key = lambda f_tuple: f_tuple[1] )))[0]
                #for image_w in listdir(data_path):
                #    if image_w.split(".")[0][:8] == label:
                #        fname.append(join(data_path,image_w))
            #fid = int(fid[-5:])-1
            #print(fname_number)
            #fname = join( data_path, sorted_fnames[fid] )
            #filelists[dataset][label].append(fname)

    for key, filelist in filelists[dataset].items():
        cl += 1
        random.shuffle(filelist)
        filelists_flat[dataset] += filelist
        labellists_flat[dataset] += np.repeat(cl, len(filelist)).tolist() 
        #print(filelists_flat[dataset][0])

for dataset in dataset_list:
    fo = open(savedir + dataset + ".json", "w")
    fo.write('{"label_names": [')
    fo.writelines(['"%s",' % item  for item in folderlist])
    fo.seek(0, os.SEEK_END) 
    fo.seek(fo.tell()-1, os.SEEK_SET)
    fo.write('],')

    fo.write('"image_names": [')
    fo.writelines(['"%s",' % item  for item in filelists_flat[dataset]])
    fo.seek(0, os.SEEK_END) 
    fo.seek(fo.tell()-1, os.SEEK_SET)
    fo.write('],')

    fo.write('"image_labels": [')
    fo.writelines(['%d,' % item  for item in labellists_flat[dataset]])
    fo.seek(0, os.SEEK_END) 
    fo.seek(fo.tell()-1, os.SEEK_SET)
    fo.write(']}')

    fo.close()
    print("%s -OK" %dataset)
