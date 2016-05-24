#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from PIL import Image
import re
import shutil
import argparse

parser = argparse.ArgumentParser(description='Scaling down images')
parser.add_argument('-p', '--percentage', type=int, dest='percentage',
                   help='scale down image by the given percentage, by default is 50%')
args = parser.parse_args()




def scale_down(imageFile, scalePercent):
    """
    Scale image down by 50% percentage.
    """
    img = Image.open(imageFile)
    width, height = img.size

    # adjust width and height by percentage
    new_width = width  * scalePercent / 100
    new_height = height * scalePercent / 100


    new_img = img.resize((int(new_width), int(new_height)), Image.ANTIALIAS)
    fileName, ext = os.path.splitext(imageFile)
    new_file_path = fileName + "_" + str(new_width) + "x" + str(new_height) + ext
    new_img.save(new_file_path)
    print ("Created " + new_file_path)
    shutil.move(new_file_path, new_folder)


#  create a new folder to store all resized images
curDir = os.getcwd()
new_folder = curDir.split('\\')[-1] + '_new'
if not os.path.exists(new_folder):
    os.makedirs(new_folder)

for file in os.listdir('.'):
    if re.match('.*\.(jpg|png)', file):
        if args.percentage:
            scale_down(file, args.percentage)
        else:
            scale_down(file, 50)



