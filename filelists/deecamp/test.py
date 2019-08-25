"""
Usage instructions:
    First download the omniglot dataset 
    and put the contents of both images_background and images_evaluation in data/omniglot/ (without the root folder)

    Then, run the following:
    cd data/
    cp -r omniglot/* omniglot_resized/
    cd omniglot_resized/
    python resize_images.py
"""
from PIL import Image
import glob
import numpy as np
import os

path_list = ["train","test","val"]
for image_path in path_list:

    all_classes = glob.glob(image_path + '/*/')
    for i, cla in enumerate(all_classes):
        all_images = glob.glob(cla + "*")
        for i in range(len(all_images)-1):
            im1 = Image.open(all_images[i])
            im2 = Image.open(all_images[i+1])
            mean = np.sum(np.array(im1)-np.array(im2))
        #im = im.resize((84,84), resample=Image.LANCZOS)
        #i += 1
            print(mean)
        #if i % 200 == 0:
        #    print(i)

