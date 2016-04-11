"""
Script that allows scaling of images
"""

import os
from PIL import Image
import re

def scale_down(imageFile, scalePercent=50):
    """
    Scale image down by 50% percentage. Will create a new 
    file with the same name plus '_small' in the same dir.
    """
    img = Image.open(imageFile)
    width, height = img.size

    # adjust width and height by percentage
    new_width = width  * scalePercent / 100
    new_height = height * scalePercent / 100


    new_img = img.resize((new_width, new_height), Image.ANTIALIAS)
    fileName, ext = os.path.splitext(imageFile)
    new_file_path = fileName + "_" + str(new_width) + "x" + str(new_height) + ext
    new_img.save(new_file_path)
    print "Created " + new_file_path





for file in os.listdir('.'):
    if re.match('.*\.(jpg|png)', file):
        scale_down(file)




