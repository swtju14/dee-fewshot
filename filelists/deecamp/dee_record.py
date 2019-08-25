#!/usr/bin/env python
# coding=utf-8
import csv
import glob
from PIL import Image, ImageFilter
#from PIL import Image
import os
from os.path import join

#path_to_image = "trainval/"
path_to_image = "test/"
new_path = "new_train"
if not os.path.exists(new_path):
    os.system("mkdir " + new_path)

all_images = glob.glob(path_to_image + "*/*/*")
print(all_images[0].split("/")[1])
for i, image in enumerate(all_images):
    img_dir = image.split("/")[1] + "_" + image.split("/")[2]
    img_name = image.split("/")[-1]

    cur_dir = new_path + "/" + img_dir + "/"
    #print(join(cur_dir,str(i) + ".jpg"))
    if not os.path.exists(cur_dir):
        os.system("mkdir " + cur_dir)
    #os.rename(image,path_to_image + img_dir + image.split("/")[-1])
    #print(image)
    #os.system("cp image" + " " + cur_dir)
    im = Image.open(image).convert("RGB")
    im = im.filter(ImageFilter.CONTOUR)
    im = im.resize((256,256),resample = Image.LANCZOS)

    for deg in [0,90,180,270]:
        rot_str = "rot_%03d"%deg
        #im = Image.open(image).draft("L", (200,200))
        rot_im = im.rotate(deg)
        mv_path = cur_dir
        rot_im.save(join(mv_path, rot_str + "_" + img_dir + "_" + img_name))
    if i%200 == 0:
        print(i)
